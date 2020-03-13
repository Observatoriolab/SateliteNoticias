<template>
  <b-row>

    <b-col md="4" style="margin-left:auto;
   margin-right:auto;
   display:flex;">

        <h6 style="padding-top: 1em"> Relevancia</h6>

        <star-rating   :increment="0.5" star-size="30"></star-rating>



    </b-col>
     <b-col md="4"  style="margin-left:auto;
   margin-right:auto;
   display:flex;">

        <h6 style="padding-top: 1em"> Irrelevancia</h6>
          <star-rating  inactive-color="#e1bad9" active-color="#cc1166"  :increment="0.5" star-size="30"></star-rating>



    </b-col>
    <b-col md="2">
      <EditionButton ></EditionButton>

      


    </b-col>

  </b-row>
  
</template>
<script>   
import StarRating from 'vue-star-rating'
import EditionButton from "./EditionButton.vue";


export default{
  components: {
    StarRating,
        EditionButton

  },
  data(){
    return {

        rating: "No Rating Selected",
        currentRating: "No Rating",
        currentSelectedRating: "No Current Rating"
    }
  },
    methods: {
        setRating: function(rating) {
          this.rating = "You have Selected: " + rating + " stars";
        },
        showCurrentRating: function(rating) {
          this.currentRating = (rating === 0) ? this.currentSelectedRating : "Click to select " + rating + " stars"
        },
        setCurrentSelectedRating: function(rating) {
          this.currentSelectedRating = "You have Selected: " + rating + " stars";
        }
      },

}
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