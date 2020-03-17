<template>


      <div style="text-align:center">
                <h4  style="padding:1em;  color:blue">Bibliografia</h4>

            <b-row style="width: 95%; text-align:center;  margin-left:auto;margin-right:auto;  color:blue" fluid>
              <!-- BIBLIOGRAPHY COMPONENT -->
              <b-col md="4 p-1" >
                <h6 >Nombre:</h6>
                <div style="padding:0.5em"></div>
                <h6 >Link:</h6>

              </b-col>

              <b-col md="5" > 
                            <b-form-input></b-form-input>
                          <b-form-input></b-form-input>

                                </b-col>

              <b-col md="3" >
                 <div class="button">
                  <b-button squared lg="4" variant="primary">Agregar</b-button>
                </div>
              </b-col>
              <!-- BIBLIOGRAPHY COMPONENT -->
            </b-row>



      </div>
</template>
<script>
export default {
  name: "Bibliography",
  props:{
    bibliographyName: String,
    bibliographyLink: String
  },
  data: () => ({
      bibliographyNameInternal: null,
      bibliographyLinkInternal: null

  }),
  methods:{
      onChange(){
        this.$emit('bibliography-change', this.bibliographyNameInternal,this.bibliographyLinkInternal)
      }
  },
};
</script>
<style lang="stylus"></style>