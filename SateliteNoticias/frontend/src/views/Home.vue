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
        <button
          @click="getQuestions"
          class="btn btn-sm btn-outline-danger"
        >
          Cancel Filter
        </button>
      </div>

      <div v-for="question in questions" :key="question.pk">
        <h2>
          <router-link
            :to="{ name: 'question', params: { slug: question.slug } }"
            class="question-link"
          >
            {{ question.title }}
          </router-link>
        </h2>
        <br />
        <p class="mb-0">
          Posted by:
          <span class="question-author">{{ question.author }}</span>
        </p>
        <br />
        <p>
          {{ question.content }}
        </p>
        <p>Answers: {{ question.answers_count }}</p>
        <hr />
          <br />
        <p class="mb-0">
          Tags:
          <span class="question-author">{{ question.tags }}</span>
        </p>
        <br />
      </div>

      <div v-if="!filterFlag" class="my-4">
        <p v-show="loadingQuestions">...loading...</p>

        <button
          v-show="next"
          @click="getQuestions"
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
      questions: [],
      next: null,
      loadingQuestions: false,
      tags: '',
      filterFlag: false,
      pageCount: null
    };
  },
  methods: {
    FilterbyTagsSearch(){
      let listTags = this.tags.split(",")
      console.log('Estos son los tags a buscar')
      console.log(listTags)
      var stringFormat = ""
      for (var i=0;i<listTags.length;i++){
        stringFormat = stringFormat+listTags[i]+"-"
      }
      stringFormat = stringFormat.substring(0, stringFormat.length-1);
      console.log('este es el stringformat de los tags que voy a usar')
      console.log(stringFormat)

      let endpoint = `/api/questions/tags/${stringFormat}/`;
      let method = "GET"
      apiService(endpoint,method)
        .then(data => {
          console.log("este es el resultado de lo que me dio el back")
          console.log(data.results)
          this.questions = data.results
          this.filterFlag = true
      });
      
    },
    getQuestions() {
      let endpoint = "/api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      console.log(this.questions)
      apiService(endpoint).then(data => {
        this.questions.push(...data.results);
        this.loadingQuestions = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getQuestions();
    console.log(this.questions);
    document.title = "Satelite de Noticias";
  }
};
</script>

<style scooped>
.question-author {
  font-weight: bold;
  color: red;
}

.question-link {
  font-weight: bold;
  color: black;
}
.question-link:hover {
  color: #343a40;
  text-decoration: none;
}
</style>
