<template>
  <div class="single-news mt-2">
    <div v-if="news" class="container">
      <h1>{{ news.title }}</h1>
      <newsActions v-if="isnewsAuthor" :slug="news.slug" />
      <br />
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ news.author }}</span>
      </p>
      <p>{{ news.created_at }}</p>
      <hr />
      <p>{{ news.content }}</p>
      <hr />
      <br />
      <p class="mb-0">
        Tags:
        <span class="author-name">{{ news.tags }}</span>
      </p>
      <br />
      <div v-if="userHasEditioned">
        <p class="edition-added">You've written an edition!</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div style="padding-bottom: 50px"></div>

          <h1>Edit the news</h1>

          <h3>Title:</h3>
          <input
            v-model="newEditionTitle"
            class="form-control"
            placeholder="Whats the title of this edition?"
          />
          <br />
          <h3>Content:</h3>
          <div class="card-block">
            <textarea
              v-model="newEditionBody"
              class="form-control"
              placeholder="Share Your Knowledge!"
              rows="5"
            ></textarea>
          </div>
          <h2>Tags:</h2>
          <input
            v-model="editionTags"
            class="form-control"
            placeholder="Any tags? (separate them by commas)"
          />
          <br />
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">
              Submit Your Edition
            </button>
          </div>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button class="btn btn-sm btn-success" @click="showForm = true">
          Edition the news
        </button>
      </div>
      <hr />
    </div>
    <div v-else>
      <h1 class="error text-center">404 - news Not Found</h1>
    </div>
    <div v-if="news" class="container">
      <EditionComponent
        v-for="edition in editions"
        :edition="edition"
        :requestUser="requestUser"
        :key="edition.id"
        @delete-edition="deleteEdition"
      />
      <div class="my-4">
        <p v-show="loadingEditions">...loading...</p>
        <button
          v-show="next"
          @click="getnewsEditions"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import EditionComponent from "@/components/Edition.vue";
import NewsActions from "@/components/NewsActions.vue";
export default {
  name: "News",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    EditionComponent,
    NewsActions
  },
  data() {
    return {
      news: {},
      editions: [],
      next: null,
      loadingEditions: false,
      newEditionTitle: null,
      newEditionBody: null,
      editionTags: [],
      error: null,
      userHasEditioned: false,
      showForm: false,
      requestUser: null
    };
  },
  computed: {
    isnewsAuthor() {
      // return true if the logged in user is also the author of the news instance
      return this.news.author === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    getnewsData() {
      // get the details of a news instance from the REST API and call setPageTitle
      let endpoint = `/api/news/${this.slug}/`;
      apiService(endpoint).then(data => {
        if (data) {
          this.news = data;
          this.userHasEditioned = data.user_has_editioned;
          this.setPageTitle(data.content);
        } else {
          this.news = null;
          this.setPageTitle("404 - Page Not Found");
        }
      });
    },
    getnewsEditions() {
      // get a page of editions for a single news from the REST API's paginated 'news Endpoint'
      let endpoint = `/api/news/${this.slug}/editions/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingEditions = true;
      apiService(endpoint).then(data => {
        this.editions.push(...data.results);
        this.loadingEditions = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      // Tell the REST API to create a new edition for this news based on the user input, then update some data properties

      if (this.newEditionBody) {
        let endpoint = `/api/news/${this.slug}/edition/`;
        apiService(endpoint, "POST", {
          title: this.newEditionTitle,
          body: this.newEditionBody,
          tags: this.editionTags
        });
        this.newEditionBody = null;
        this.showForm = false;
        this.userHasEditioned = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty edition!";
      }
    },
    async deleteEdition(edition) {
      // delete a given edition from the editions array and make a delete request to the REST API
      let endpoint = `/api/editions/${edition.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.editions, this.editions.indexOf(edition));
        this.userHasEditioned = false;
      } catch (err) {
        console.log(err);
      }
    }
  },
  created() {
    this.getnewsData();
    this.getnewsEditions();
    this.setRequestUser();
  }
};
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #dc3545;
}

.edition-added {
  font-weight: bold;
  color: green;
}

.error {
  font-weight: bold;
  color: red;
}
</style>
