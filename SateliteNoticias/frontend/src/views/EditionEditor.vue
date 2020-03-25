<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Edition</h1>
    <form @submit.prevent="onSubmit">
      <h3>Title:</h3>
      <input
        v-model="editionTitle"
        class="form-control"
        placeholder="Whats the title of this edition?"
      />
      <br />
      <h3>Content::</h3>
      <textarea v-model="editionBody" class="form-control" rows="3"></textarea>
      <br />
      <h2>Tags:</h2>
      <input
        v-model="editionTags"
        class="form-control"
        placeholder="Any tags? (separate them by commas)"
      />
      <br />
      <button type="submit" class="btn btn-success">
        Publish your edition
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "EditionEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      newslug: null,
      editionTitle: null,
      editionBody: null,
      editionTags: [],
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.editionBody) {
        let endpoint = `/api/editions/${this.id}/`;
        apiService(endpoint, "PUT", {
          title: this.editionTitle,
          body: this.editionBody,
          tags: this.editionTags
        }).then(() => {
          this.$router.push({
            name: "news",
            params: { slug: this.newslug }
          });
        });
      } else {
        this.error = "You can't submit an empty edition!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the edition's data from the REST API and set two data properties for the component
    let endpoint = `/api/editions/${to.params.id}/`;
    let data = await apiService(endpoint);
    //console.log('esta es la data cuando voy a editar una pregunta')
    //console.log(data)
    return next(
      vm => (
        (vm.editionBody = data.body),
        (vm.newslug = data.news_slug),
        (vm.editionTags = data.tags),
        (vm.editionTitle = data.title)
      )
    );
  }
};
</script>
