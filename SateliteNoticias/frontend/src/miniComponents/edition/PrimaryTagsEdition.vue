<template>
  <div style =" width: 90%; margin-left:auto;margin-right:auto">
    <!-- PRIMARY TAGS EDITION COMPONENT -->
    <b-row>
              <b-col md="4">
                <h5 class="text-primary">#EJE</h5>

                <h5 class="text-primary p-1">#PAIS</h5>
                <h5 class="text-primary p-1">#ORGANISMO</h5>
                <h5 class="text-primary p-1">#FECHA</h5>

              </b-col>
              <b-col md="4">
                  <b-dropdown
                    split
                    split-variant="outline-primary"
                    variant="primary"
                    text="Ejes"
                  >
                    <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
                    <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
                    <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
                  </b-dropdown>

                  <b-dropdown
                    split
                    split-variant="outline-primary"
                    variant="primary"
                    text="Pais"
                  >
                    <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
                    <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
                    <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>

                  </b-dropdown>


                    <b-dropdown
                      split
                      split-variant="outline-primary"
                      variant="primary"
                      text="Organismo"
                    >
                      <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
                      <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
                      <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
                    </b-dropdown>

                      <b-dropdown
                        split
                        split-variant="outline-primary"
                        variant="primary"
                        text="Fecha"
                      >
                        <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
                        <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
                        <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
                      </b-dropdown>

                      
              </b-col>
              <b-col md="4">
                <div class="buttonn">
                  <b-button squared lg="4" variant="primary">Agregar</b-button>
                </div>

                <div class="buttonn ">
                  <b-button squared lg="4" variant="primary">Agregar</b-button>
                </div>
                <div class="buttonn ">
                  <b-button squared lg="4" variant="primary">Agregar</b-button>
                </div>
                <div class="buttonn ">
                  <b-button squared lg="4" variant="primary">Agregar</b-button>
                </div>
              </b-col>


        </b-row>

    <!-- PRIMARY TAGS EDITION COMPONENT -->
  </div>
</template>
<script>
export default {
  name: "PrimaryTagsEdition"
};
</script>
<style scope>
.buttonn{
  border:1px solid white;
}

</style>