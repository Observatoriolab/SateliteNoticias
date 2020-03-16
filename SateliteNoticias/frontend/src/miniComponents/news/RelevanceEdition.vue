<template>
  <div style="width: 100%; text-align:center;   border:1px solid blue; color:blue; padding: 1em 0px 1em" fluid>
    <Relevance :relevance="relevance" :irrelevance="irrelevance" @clicked-edition="clickedEdition"></Relevance>
  </div>
</template>
<script>
import Relevance from "./Relevance.vue";
export default {
  name: "RelevanceEdition",
  props:{
    relevance:Number,
    irrelevance:Number
  },
  components: {
    Relevance,
  },
  methods:{
    clickedEdition() {
        this.$emit('clicked-edition')
    }
  },
  created(){
    console.log(this)
  }
};
</script>
<style lang="stylus"></style>