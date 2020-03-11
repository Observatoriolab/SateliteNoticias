<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Answer</h1>
    <form @submit.prevent="onSubmit">
      <textarea v-model="answerBody" class="form-control" rows="3"></textarea>
      <br />
      <h2>Tags:</h2>
          <input
            v-model="answerTags"
            class="form-control"
            placeholder="Any tags? (separate them by commas)"
          />
      <br>
      <button type="submit" class="btn btn-success">Publish your answer</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      newslug: null,
      answerBody: null,
      answerTags: [],
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody, tags: this.answerTags }).then(() => {
          this.$router.push({
            name: "news",
            params: { slug: this.newslug }
          });
        });
      } else {
        this.error = "You can't submit an empty answer!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    console.log('esta es la data cuando voy a editar una pregunta')
    console.log(data)
    return next(
      vm => (
        (vm.answerBody = data.body), (vm.newslug = data.news_slug), (vm.answerTags = data.tags)
      )
    );
  }
};
</script>
