<template>
    <!-- PRIMARY TAGS COMPONENT -->

    <div style="width: 96%;  margin-left:auto;margin-right:auto">

          <b-row style="color: blue;border: 1px solid blue; text-align:center;" fluid>

                      <b-col md="3" > 
                        <div style="padding: 5px"></div>

                        <h6>EJE</h6>
                          <b-dropdown split split-variant="outline-primary" variant="primary" text="#EJE" class="m-2">
                          <b-dropdown-item href="#">Eje 1</b-dropdown-item>
                          <b-dropdown-item href="#">Eje 2</b-dropdown-item>
                          <b-dropdown-item href="#">Eje 3</b-dropdown-item>
                        </b-dropdown>
                      </b-col>
                  
                    <b-col md="3" >
                        <div style="padding: 5px"></div>

                        <h6>PAIS/REGION</h6>
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
                        
                    </b-col>



                    <b-col md="3" >
                        <div style="padding: 5px"></div>

                         <h6>ORGANISMO/ENTIDAD</h6>

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
                    </b-col>


                      <b-col md="3" > 
                        <div style="padding: 5px"></div>

                        <h6>FECHA</h6>
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

                      </b-col>

            </b-row>

      
    </div>
            



  

    
    <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>

export default {
  name: "PrimaryTags",
  components:{


    },
  data() {
    return {
    };
  },
};
</script>
<style lang="stylus"></style>