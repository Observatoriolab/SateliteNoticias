<template>
  <div class="news-actions">
    <router-link
      :to="{ name: 'news-editor', params: { slug: slug } }"
      class="btn btn-sm btn-outline-secondary mr-1"
      >Edit
    </router-link>
    <button class="btn btn-sm btn-outline-danger" @click="deletenews">
      Delete
    </button>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "newsActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deletenews() {
      console.log('aqui deberia estar el slug')
      console.log(this.slug)
      let endpoint = `/api/news/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (err) {
        console.log(err);
      }
    }
  }
};
</script>
