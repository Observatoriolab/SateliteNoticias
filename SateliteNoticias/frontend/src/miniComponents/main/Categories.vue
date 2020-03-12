<template>
  <b-col md="2">
    <div class="dropdown p-4">
      <b-dropdown class="mx-1" block variant="primary" right text="Categorias">
        <b-dropdown-item>1</b-dropdown-item>
        <b-dropdown-item>2</b-dropdown-item>
        <b-dropdown-item>3</b-dropdown-item>
        <b-dropdown-item>4</b-dropdown-item>
        <b-dropdown-item>5</b-dropdown-item>
        <b-dropdown-item>6</b-dropdown-item>
        <b-dropdown-item>7</b-dropdown-item>
        <b-dropdown-item>8</b-dropdown-item>
      </b-dropdown>
      <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a class="dropdown-item disabled" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <a class="dropdown-item" href="#">Something else here</a>
      </div>
    </div>
  </b-col>
</template>
<script>
export default {
  name: "Categories"
};
</script>
<style lang="stylus"></style>