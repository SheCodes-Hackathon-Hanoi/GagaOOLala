import { ref } from "vue";
import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api";
export default function useTravel() {
  const travels = ref([]);
  const travel = ref([]); //array
  const errors = ref({}); //object

  const getRecommendTrip = async () => {
    const response = await axios.get("/recommend/",{
      data: {
        user_id: 1,
      },
    });
    travels.value = response.data;
  };
  const getTrendingTrip = async () => {
    const response = await axios.get("/trending/");
    return response.data;
    // travels.value = response.data;
    // console.log(travels.value);
  };

  return {
    travel,
    travels,
    errors,
    getRecommendTrip,
    getTrendingTrip,
  };
}
