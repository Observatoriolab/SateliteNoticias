<template>
  <b-container fluid>
    <!-- BIBLIOGRAPHY COMPONENT -->
    <b-col md="3" class="p-2">
      <h4 class="text-primary">BIBLIOGRAFIA</h4>
    </b-col>
    <b-col md="3" class="p-2">
      <h4 class="text-primary">Nombre</h4>
      <div>
        <b-dropdown
          split
          split-variant="outline-primary"
          variant="primary"
          text="       "
          class="m-2 p-2"
        >
          <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
          <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
          <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
        </b-dropdown>
      </div>
    </b-col>
    <b-col md="3" class="p-2">
      <b-input-group class="mt-3">
        <template v-slot:append>
          <b-input-group-text>
            <strong class="text-primary">link</strong>
          </b-input-group-text>
        </template>
        <b-form-input></b-form-input>
      </b-input-group>
    </b-col>
    <b-col md="3"></b-col>
    <!-- BIBLIOGRAPHY COMPONENT -->
  </b-container>
</template>
<script>
export default {
  name: "Bibliography"
};
</script>
<style lang="stylus"></style>