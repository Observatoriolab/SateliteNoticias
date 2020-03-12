<template>
  <div>
    <!-- NEWS EDITION COMPONENT -->
    <h3 class="text-primary text-center p-2">Edición</h3>
    <h4 class="text-primary p-2">Titulo</h4>
    <b-form-textarea
      id="textarea"
      placeholder="Edición titulo..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>

    <h4 class="text-primary p-2">Contenido</h4>
    <b-form-textarea
      id="textarea"
      placeholder="Edición contenido..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
    <pre class="mt-3 mb-0"></pre>

    <!-- NEWS EDITION COMPONENT -->
  </div>
</template>
<script>
export default {
  name: "NewsEdition"

};
</script>
<style lang="stylus"></style>