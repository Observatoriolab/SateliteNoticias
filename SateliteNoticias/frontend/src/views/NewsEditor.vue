<template>
  <div class="container mt-2">
    <h1 class="mb-3">Post a piece of news</h1>
    <form @submit.prevent="onSubmit">
      <h2>Title:</h2>
      <input
        v-model="news_title"
        class="form-control"
        placeholder="Whats the title of this news?"
      />
      <br />
      <h2>Content:</h2>
      <br />
      <textarea
        v-model="news_body"
        class="form-control"
        rows="3"
        placeholder="What do you want to inform us about?"
      ></textarea>
      <br />
      <h2>Tags:</h2>
      <input
        v-model="news_tags"
        class="form-control"
        placeholder="Whats the title of this news?"
      />
      <br />
      <button type="submit" class="btn btn-success">Publish</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "NewsEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      news_title: null,
      news_body: null,
      news_tags: [],
      error: null
    };
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a news Instance
      if (!this.news_title) {
        this.error = "You can't send an empty news!";
      } else if (this.news_title.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/news/";
        let method = "POST";
        //console.log('este es el slug que EXISTE WN')
        //console.log(this.$route.params.slug)
        if (this.$route.params.slug !== undefined) {
          endpoint += `${this.$route.params.slug}/`;
          method = "PUT";
        }
        apiService(endpoint, method, {
          title: this.news_title,
          content: this.news_body,
          tags: this.news_tags
        }).then(news_data => {
          //console.log("esta es la data que me dio en el front");
          //console.log(news_data);
          this.$router.push({
            name: "news",
            params: { slug: news_data.slug }
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a news, then get the news's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/news/${to.params.slug}/`;
      let data = await apiService(endpoint);
      //console.log(data);
      return next(
        vm => (
          (vm.news_title = data.title), (vm.news_body = data.content), (vm.news_tags = data.tags)
        )
      );
    } else {
      return next();
    }
  },
  created() {
    document.title = "Editor - newsTime";
  }
};
</script>
