<template>
  <div
    style="width:90%; text-align:center; margin-right:auto; margin-left:auto"
  >
    <!-- NEWS EDITION COMPONENT -->
    <h3 class="text-primary" style="margin-center:auto">Edición</h3>
    <h4 class="text-primary p-1">Titulo</h4>
    <b-form-input
      id="input"
      placeholder="Edición titulo..."
      v-model="titleInternal"
      v-on:change="onChange"
    ></b-form-input>

    <h4 class="text-primary p-2">Contenido</h4>
    <b-form-textarea
      id="textarea"
      placeholder="Edición contenido..."
      rows="3"
      max-rows="15"
      v-model="bodyInternal"
      style="height:18em"
      v-on:change="onChange"
    ></b-form-textarea>
    <pre class="mt-3 mb-0"></pre>

    <!-- NEWS EDITION COMPONENT -->
  </div>
</template>
<script>
export default {
  name: "NewsEdition",
  props: {
    title: String,
    body: String
  },

  data: () => ({
    titleInternal: "",
    bodyInternal: ""
  }),
  methods: {
    onChange() {
      //console.log('pase por aqui')
      this.$emit("news-change", this.titleInternal, this.bodyInternal);
    }
  },

  created() {
    //console.log('los props')
    //console.log(this.title)
    //console.log(this.body)
    this.titleInternal = this.title;
    this.bodyInternal = this.body;
  }
};
</script>
<style lang="stylus"></style>
