<template>
  <div class="home">
    <div class="container">
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import {apiService} from "../common/api.service"
export default {
  name: "home",
  data() {
    return {
      questions: []
    }
  },
  methods : {
    getQuestions() {
      let endpoint = "api/questions/";
      apiService(endpoint)
        .then (data => {
          this.questions.push(...data.results)
        })    
    }
  }
};
</script>
