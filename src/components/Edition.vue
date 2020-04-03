<template>
  <div class="single-edition">
    <p class="text-muted">
      <strong> {{ edition.author }}</strong> &#8901; {{ edition.created_at }}
    </p>
    <p>{{ edition.body }}</p>
    <p class="mb-0">
      Tags:
      <span>{{ edition.tags }}</span>
    </p>
    <div v-if="isEditionAuthor">
      <router-link
        :to="{ name: 'edition-editor', params: { id: edition.id } }"
        class="btn btn-sm btn-outline-secondary mr-1"
      >
        Edit
      </router-link>
      <button
        @click="triggerDeleteEdition"
        class="btn btn-sm btn-outline-danger"
      >
        Delete
      </button>
    </div>

    <div v-else>
      <button
        class="btn btn-sm"
        @click="toggleLike"
        :class="{
          'btn-danger': userLikedEdition,
          'btn-outline-danger': !userLikedEdition
        }"
      >
        <strong> Like [{{ likesCounter }}]</strong>
      </button>
    </div>

    <hr />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "EditionComponent",
  props: {
    edition: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      userLikedEdition: this.edition.user_has_voted,
      likesCounter: this.edition.likes_count
    };
  },
  computed: {
    isEditionAuthor() {
      return this.edition.author == this.requestUser;
    }
  },
  methods: {
    toggleLike() {
      this.userLikedEdition === false
        ? this.likeEdition()
        : this.unLikeEdition();
    },
    likeEdition() {
      this.userLikedEdition = true;
      this.likesCounter += 1;
      let endpoint = `/api/editions/${this.edition.id}/like/`;
      apiService(endpoint, "POST");
    },
    unLikeEdition() {
      this.userLikedEdition = false;
      this.likesCounter -= 1;
      let endpoint = `/api/editions/${this.edition.id}/like/`;
      apiService(endpoint, "DELETE");
    },
    triggerDeleteEdition() {
      this.$emit("delete-edition", this.edition);
    }
  }
};
</script>
