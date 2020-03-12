<template>
  <b-row style="width: 100%; text-align:center;  margin-left:auto;margin-right:auto; border:1px solid blue; color:blue" fluid>
    <!-- BIBLIOGRAPHY COMPONENT -->
    <div style="padding-left:5em"></div>
    <b-col md="3" >
      <div style="padding:10px"></div>
      <h4 class="text-primary">Bibliografia</h4>
    </b-col>
      <div style="padding:10px"></div>

                      <b-row md="3" > 
                                                <h6  style="padding-top: 1.5em">Nombre:</h6>


                          <b-dropdown split split-variant="outline-primary" variant="primary" text="Reprentativo" class="m-3">
                          <b-dropdown-item href="#">Eje 1</b-dropdown-item>
                          <b-dropdown-item href="#">Eje 2</b-dropdown-item>
                          <b-dropdown-item href="#">Eje 3</b-dropdown-item>
                        </b-dropdown>
                      </b-row>
    <div style="padding-left:3em"></div>

    <b-col md="3" >
      <b-input-group class="mt-3">
        <template v-slot:append>
          <b-input-group-text>
            <strong class="text-primary">link</strong>
          </b-input-group-text>
        </template>
        <b-form-input></b-form-input>
      </b-input-group>
    </b-col>
    <!-- BIBLIOGRAPHY COMPONENT -->
  </b-row>
</template>
<script>
export default {
  name: "Bibliography"
};
</script>
<style lang="stylus"></style>