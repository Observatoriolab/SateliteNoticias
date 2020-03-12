<template>
  <div>
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