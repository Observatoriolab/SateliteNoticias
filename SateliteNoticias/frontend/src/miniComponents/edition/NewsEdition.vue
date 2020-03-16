<template>
  <div style="width:90%; text-align:center; margin-right:auto; margin-left:auto">
    <!-- NEWS EDITION COMPONENT -->
    <h3 class="text-primary text-center p-2">Edición</h3>
    <h4 class="text-primary p-1">Titulo</h4>
    <b-form-input
      id="input"
      placeholder="Edición titulo..."
    ></b-form-input>

    <h4 class="text-primary p-2">Contenido</h4>
    <b-form-textarea
      id="textarea"
      placeholder="Edición contenido..."
      rows="3"
      max-rows="15"
      style="height:18em"
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
<style lang="stylus">


</style>