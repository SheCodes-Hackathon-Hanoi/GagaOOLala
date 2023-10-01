import { ref } from "vue";
import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api";
export default function useTravel() {
  const travels = ref([]);
  const travel = ref([]); //array
  const errors = ref({}); //object

  const getRecommendTrip = async () => {
    const data = { user_id: 1 };
    const response = await axios.post("/recommend/", data);
    travels.value = response.data;
    console.log(travels.value);
  };
  const getTrendingTrip = async () => {
    const response = await axios.get("/trending/");
    travels.value = response.data;
  };
  const getTravel = async (id) => {
    const response = await axios.get("/travel/" + id);
    travel.value = response.data;
  };

  return {
    travel,
    travels,
    errors,
    getRecommendTrip,
    getTrendingTrip,
    getTravel,
  };
}
