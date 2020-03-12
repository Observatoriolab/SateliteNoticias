<template>
  <div style="width: 100%; text-align:center;  margin-left:auto;margin-right:auto; border:1px solid blue; color:blue; padding: 1em 0px 1em" fluid>
    <Relevance></Relevance>
    <EditionButton></EditionButton>
  </div>
</template>
<script>
import Relevance from "./Relevance.vue";
import EditionButton from "./EditionButton.vue";
export default {
  name: "RelevanceEdition",
  components: {
    Relevance,
    EditionButton
  }
};
</script>
<style lang="stylus"></style>