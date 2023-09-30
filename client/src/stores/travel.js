import { ref } from "vue";
import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api";
export default function useTravel() {
  const travels = ref([]);
  const travel = ref([]); //array
  const errors = ref({}); //object

  const getRecommendTrip = async () => {
    const response = await axios.get("/recommend/", {
      headers: { "Access-Control-Allow-Origin": "*" },
      data: {
        user_id: 1,
      },
    });
    console.log(response.data);
    travels.value = response.data;
  };
  const getTrendingTrip = async () => {
    const response = await axios.get("/trending/");
    console.log(response.data);
    travels.value = response.data;
  };

  return {
    travel,
    travels,
    errors,
    getRecommendTrip,
    getTrendingTrip,
  };
}
