<template>
  <div class="home">
    <div class="container mt-4">
      <div class="my-4">
        <h2>Tags a buscar:</h2>
        <input
          v-model="tags"
          class="form-control"
          placeholder="Any tags to search for? (separate them by commas by the meantime)"
        />
        <br />
        <button
          @click="FilterbyTagsSearch()"
          class="btn btn-sm btn-outline-success"
        >
          Filter news by tags
        </button>
        <button @click="cancelFilter" class="btn btn-sm btn-outline-danger">
          Cancel Filter
        </button>
      </div>

      <div v-for="news in news" :key="news.pk">
        <h2>
          <router-link
            :to="{ name: 'news', params: { slug: news.slug } }"
            class="news-link"
          >
            {{ news.title }}
          </router-link>
        </h2>
        <br />
        <p class="mb-0">
          Posted by:
          <span class="news-author">{{ news.author }}</span>
        </p>
        <br />
        <p>
          {{ news.content }}
        </p>
        <p>Editions: {{ news.editions_count }}</p>
        <hr />
        <br />
        <p class="mb-0">
          Tags:
          <span class="news-author">{{ news.tags }}</span>
        </p>
        <br />
      </div>

      <div v-if="!filterFlag" class="my-4">
        <p v-show="loadingnews">...loading...</p>

        <button
          v-show="next"
          @click="getnews"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      news: [],
      next: null,
      loadingnews: false,
      tags: null,
      filterFlag: false,
      pageCount: null
    };
  },
  methods: {
    cancelFilter() {
      //vaciar las preguntas para poderlas preguntar denuevo
      this.news.splice(0);
      this.filterFlag = false;
      this.tags = null;
      this.getnews();
    },
    FilterbyTagsSearch() {
      if (this.tags !== null) {
        if (this.tags.length !== 0) {
          let listTags = this.tags.split(",");
          var stringFormat = "";
          for (var i = 0; i < listTags.length; i++) {
            stringFormat = stringFormat + listTags[i] + "-";
          }
          stringFormat = stringFormat.substring(0, stringFormat.length - 1);

          let endpoint = `/api/news/tags/${stringFormat}/`;
          let method = "GET";
          apiService(endpoint, method).then(data => {
            this.news = data.results;
            this.filterFlag = true;
            this.next = null;
          });
        } else {
          alert("esta vacio");
        }
      } else {
        alert("esta vacio");
      }
    },
    getnews() {
      let endpoint = "/api/news/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingnews = true;
      apiService(endpoint).then(data => {
        this.news.push(...data.results);
        this.loadingnews = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getnews();
    document.title = "Satelite de Noticias";
  }
};
</script>

<style scooped>
.news-author {
  font-weight: bold;
  color: red;
}

.news-link {
  font-weight: bold;
  color: black;
}
.news-link:hover {
  color: #343a40;
  text-decoration: none;
}
</style>
