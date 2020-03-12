<template>
  <b-container fluid>
    <!-- PRIMARY TAGS COMPONENT -->

    <b-col md="3" class="p-2">
      <div>
        <b-dropdown split split-variant="outline-primary" variant="primary" text="#EJE" class="m-2">
          <b-dropdown-item href="#">Eje 1</b-dropdown-item>
          <b-dropdown-item href="#">Eje 2</b-dropdown-item>
          <b-dropdown-item href="#">Eje 3</b-dropdown-item>
        </b-dropdown>
      </div>
    </b-col>

    <b-col md="3" class="p-2">
      <div>
        <b-dropdown
          split
          split-variant="outline-primary"
          variant="primary"
          text="#PAIS"
          class="m-2"
        >
          <b-dropdown-item href="#">Pais 1</b-dropdown-item>
          <b-dropdown-item href="#">Pais 2</b-dropdown-item>
          <b-dropdown-item href="#">Pais 3</b-dropdown-item>
        </b-dropdown>
      </div>
    </b-col>
    <b-col md="3" class="p-2">
      <div>
        <b-dropdown
          split
          split-variant="outline-primary"
          variant="primary"
          text="#ORGANISMO"
          class="m-2"
        >
          <b-dropdown-item href="#">Organismo 1</b-dropdown-item>
          <b-dropdown-item href="#">Organismo 2</b-dropdown-item>
          <b-dropdown-item href="#">Organismo 3</b-dropdown-item>
        </b-dropdown>
      </div>
    </b-col>
    <b-col md="3" class="p-2">
      <div>
        <b-dropdown
          split
          split-variant="outline-primary"
          variant="primary"
          text="#FECHA"
          class="m-2"
        >
          <b-dropdown-item href="#">Fecha 1</b-dropdown-item>
          <b-dropdown-item href="#">Fecha 2</b-dropdown-item>
          <b-dropdown-item href="#">Fecha 3</b-dropdown-item>
        </b-dropdown>
      </div>
    </b-col>
    <!-- PRIMARY TAGS COMPONENT -->
  </b-container>
</template>
<script>
export default {
  name: "PrimaryTags"
};
</script>
<style lang="stylus"></style>