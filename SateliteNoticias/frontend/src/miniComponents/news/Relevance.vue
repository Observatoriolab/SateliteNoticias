<template>
  <b-row>
    <b-col
      md="4"
      style="margin-left:auto;
   margin-right:auto;
   display:flex;"
    >
      <h6 style="padding-top: 1em">Relevancia</h6>

      <star-rating
        v-model="localRelevance"
        :increment="0.5"
        :star-size="starSize"
      ></star-rating>
    </b-col>
    <b-col
      md="4"
      style="margin-left:auto;
                    margin-right:auto;
                    display:flex;"
    >
      <h6 style="padding-top: 1em">Irrelevancia</h6>
      <star-rating
        v-model="localIrrelevance"
        inactive-color="#e1bad9"
        active-color="#cc1166"
        :increment="0.5"
        :star-size="starSize"
      ></star-rating>
    </b-col>
    <b-col md="2">
      <EditionButton @clicked-edition="clickedEdition"></EditionButton>
    </b-col>
  </b-row>
</template>
<script>
import StarRating from "vue-star-rating";
import EditionButton from "./EditionButton.vue";

export default {
  name: "Relevance",
  props: {
    relevance: Number,
    irrelevance: Number
  },
  components: {
    StarRating,
    EditionButton
  },
  data() {
    return {
      rating: "No Rating Selected",
      currentRating: "No Rating",
      currentSelectedRating: "No Current Rating",
      starSize: 30,
      localRelevance: null,
      localIrrelevance: null
    };
  },
  methods: {
    clickedEdition() {
      this.$emit("clicked-edition");
    }
  },
  created() {
    //console.log(this.relevance)
    this.localRelevance = this.$props.relevance;
    this.localIrrelevance = this.$props.irrelevance;
  }
};
</script>
<style scoped>
.rating-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
}
</style>
