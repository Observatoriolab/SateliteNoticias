<template>
  <div :key="updateNews">
    <b-row   v-show="localIrrelevanceFlag||localRelevanceFlag">
     
    
      <b-col
              md="4"
            >
      <div v-show="localRelevanceFlag">Gracias por tu opinion!</div>

      </b-col>
       <b-col
              md="1"
            
            >

      </b-col>
      <b-col
              md="4"
             
            >
      <div  v-show="localIrrelevanceFlag">Gracias por tu opinion!</div>


      </b-col>



    </b-row>
    <b-row >
        <b-col
              md="4"
              style="margin-left:auto;
          margin-right:auto;
          display:flex;"
            >
              <h6 style="padding-top: 1em">Relevancia</h6>

              <star-rating
                :rating="averageRelevance"
                v-model="localRelevance"
                :increment="0.5"
                :star-size="starSize"
                :read-only="localRelevanceFlag"
                @rating-selected="setRating(true)"
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
            :rating="averageIrrelevance"
            v-model="localIrrelevance"
            inactive-color="#e1bad9"
            active-color="#cc1166"
            :increment="0.5"
            :star-size="starSize"
            :read-only="localIrrelevanceFlag"
            @rating-selected="setRating(false)"
          ></star-rating>
        </b-col>
        <b-col md="2">
          <EditionButton @clicked-edition="clickedEdition"></EditionButton>
        </b-col>


    </b-row>
    <b-row >
     
    
      <b-col
              md="4"
            >
       <div v-show="newsPiece.relevance_count !== 0">Basada en {{newsPiece.relevance_count}} opiniones </div>

      </b-col>
       <b-col
              md="1"
            >

      </b-col>
      <b-col
              md="4"
             
            >
       <div v-show="newsPiece.irrelevance_count !== 0">Basada en {{newsPiece.irrelevance_count}} opiniones </div>

      </b-col>



    </b-row>
   
  </div>
</template>
<script>
import StarRating from "vue-star-rating";
import EditionButton from "./EditionButton.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "Relevance",
  props: {
    relevance: Number,
    irrelevance: Number,
    slug:String,
    newsPiece:Object,
    updateNews:Number
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
      averageRelevance: null,
      averageIrrelevance: null,
      localRelevance:null,
      localIrrelevance:null,
      localRelevanceFlag:false ,
      localIrrelevanceFlag: false
    };
  },
  methods: {
    setRating(bool){
        this.editnews(bool)
    },
    clickedEdition() {
      this.$emit("clicked-edition");
    },
    editnews(bool) {
      var endpoint;
      endpoint = `/api/news/${this.newsPiece.id}/rating/`;
      if(bool){
          apiService(endpoint, "POST",{localRelevance:this.localRelevance, type:true});
      }
      else{
          apiService(endpoint, "POST",{localIrrelevance:this.localIrrelevance, type:false});

      }
    }
     
  },
  beforeUpdate(){

    this.localRelevance = this.$props.newsPiece.relevance_average;
    this.localIrrelevance = this.$props.newsPiece.irrelevance_average;
    this.localRelevanceFlag = this.$props.newsPiece.user_has_relevanced;
    this.localIrrelevanceFlag = this.$props.newsPiece.user_has_irrelevanced;
  },
  created() {
    //(this.relevance)
    this.localRelevance = this.$props.newsPiece.relevance_average;
    this.localIrrelevance = this.$props.newsPiece.irrelevance_average;
    this.localRelevanceFlag = this.$props.newsPiece.user_has_relevanced;
    this.localIrrelevanceFlag = this.$props.newsPiece.user_has_irrelevanced;
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
