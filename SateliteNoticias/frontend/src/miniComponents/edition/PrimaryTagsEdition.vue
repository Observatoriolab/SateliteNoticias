<template>
  <div>
    <!-- PRIMARY TAGS EDITION COMPONENT -->
    <b-row>
      <b-col md="4">
        <h4 class="text-primary">#EJE</h4>
      </b-col>
      <b-col md="4">
        <div>
          <b-dropdown
            split
            split-variant="outline-primary"
            variant="primary"
            text="Ejes"
            class="m-2"
          >
            <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
            <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
            <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
          </b-dropdown>
        </div>
      </b-col>
      <b-col md="4">
        <div class="buttonn">
          <b-button squared lg="4" variant="primary">Agregar</b-button>
        </div>
      </b-col>
    </b-row>

    <h4 class="text-primary p-1">#PAIS</h4>
    <h4 class="text-primary p-1">#ORGANISMO</h4>
    <h4 class="text-primary p-1">#PAIS</h4>
    <h4 class="text-primary p-2">LINK</h4>

    <div>
      <b-dropdown
        split
        split-variant="outline-primary"
        variant="primary"
        text="Pais"
        class="m-2 p-1"
      >
        <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
      </b-dropdown>
    </div>
    <div>
      <b-dropdown
        split
        split-variant="outline-primary"
        variant="primary"
        text="Organismo"
        class="m-2 p-1"
      >
        <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
      </b-dropdown>
    </div>
    <div>
      <b-dropdown
        split
        split-variant="outline-primary"
        variant="primary"
        text="Fecha"
        class="m-2 p-1"
      >
        <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
        <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
      </b-dropdown>
    </div>

    <div class="buttonn p-4">
      <b-button squared lg="4" variant="primary">Agregar</b-button>
    </div>
    <div class="buttonn p-4">
      <b-button squared lg="4" variant="primary">Agregar</b-button>
    </div>
    <div class="buttonn p-4">
      <b-button squared lg="4" variant="primary">Agregar</b-button>
    </div>
    <!-- PRIMARY TAGS EDITION COMPONENT -->
  </div>
</template>
<script>
export default {
  name: "PrimaryTagsEdition"
};
</script>
<style lang="stylus"></style>