<template>
    <b-container class="bv-example-row">
     <b-row>
	        <b-col md="9">
					<h3 class="text-primary text-center p-4"  >
						Satelite de Noticias 
					</h3>
				</b-col>
		    <b-col md="3">
					<b-row>
						<b-col md="6">
							 
							<b-button variant="primary" size="sm">Configuración</b-button>
						</b-col>
						<b-col md="6">
							 
							<b-button variant="primary" size="sm">Usuario</b-button>
						</b-col>
					</b-row>
				</b-col>
	</b-row>

	<b-row>
		<b-col md="12">
		
			<b-row>
				<b-col md="2">
					    <div class="dropdown p-4">
						 
						               <b-dropdown class="mx-1" block variant="primary" right text="Categorias">
                                           <b-dropdown-item>1 </b-dropdown-item>
                                           <b-dropdown-item>2</b-dropdown-item>
                                           <b-dropdown-item>3</b-dropdown-item>
                                           <b-dropdown-item>4</b-dropdown-item>
                                           <b-dropdown-item>5</b-dropdown-item>
                                           <b-dropdown-item>6</b-dropdown-item>
                                           <b-dropdown-item>7</b-dropdown-item>
                                           <b-dropdown-item>8</b-dropdown-item>
                                        </b-dropdown>
						       <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
							             <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
						       </div>
					    </div>
				</b-col> 
            
		            <b-col md="7">
					         <b-row>
						         <b-col md="4">
							           <div class="button p-4">
							            <b-button squared  lg="4" variant="primary" >Trending</b-button>
							           </div>
						          </b-col>
						        <b-col md="4">
						        </b-col>
						          <b-col md="4">
							            <div class="buttonn p-4">
							            <b-button  squared lg="4" variant="primary">Buscar</b-button>
							            </div>
						           </b-col>
					        </b-row>
                        
			        <b-row>
						<b-col md="12">
							<b-row>
								<b-col md="12">
									   <b-jumbotron bg-variant="white" header="Titulo Noticias" text-variant="primary" border-variant="primary" lead="Link:www.páginawb.cl" >
										 <p>Resumen Noticias</p>
										     <b-button lg="4" variant="outline-primary" href="#">Seguir leyendo</b-button>
											 <div>
                                                  <b-dropdown
                                                  split
                                                  split-variant="outline-primary"
                                                  variant="primary"
                                                  text="Lista de editores"
                                                  class="m-2"
                                                   >
                                                  <b-dropdown-item href="#">Action</b-dropdown-item>
                                                  <b-dropdown-item href="#">Another action</b-dropdown-item>
                                                  <b-dropdown-item href="#">Something else here...</b-dropdown-item>
                                                 </b-dropdown>
                                                 </div>
                                       </b-jumbotron>
								</b-col>
						    </b-row>
							
					<b-row >
                    
						
						<b-col md="12" class="p-3" >
                                    
									 <h7 class="text-primary text-right" >
										  #Visitas=200
									  </h7>
						</b-col >
                    
					</b-row>
		                <b-row>
							<b-col md="3" class="p-2">
									<div>
                                                  <b-dropdown
                                                  split
                                                  split-variant="outline-primary"
                                                  variant="primary"
                                                  text="#EJE"
                                                  class="m-2"
                                                   >
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
						</b-row>
							<b-row>
								<b-col md="12" class="p-5">
								</b-col>
							</b-row>
							<b-row>
								<b-col md="3" class="p-2">
									<h7 class="text-primary">
										BIBLIOGRAFIA
									</h7>
								</b-col>
								<b-col md="3" class="p-2">
									<h7 class="text-primary">
										Nombre
									</h7>
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
                                        <b-input-group-text><strong class="text-primary">link</strong></b-input-group-text>
                                        </template>
                                        <b-form-input></b-form-input>
                                        </b-input-group>
								    </b-col>
								         <b-col md="3">
								         </b-col>
							</b-row>
							<b-row>
								<b-col md="6" class="p-2">
								</b-col>
								     <b-col md="6" class="p-2">
									    <b-button   lg="4" variant="outline-primary">Editar</b-button>
								     </b-col>
							</b-row>
						
							  
				     </b-col>
			        </b-row>
		            </b-col>
				<b-col md="3" class="p-2 bg-light">
				
				
				<div>
				  <h3 class="text-primary text-center p-2">
										Edición 
									</h3>
				  <h7 class="text-primary p-2">
										Titulo
									</h7>
                  <b-form-textarea
                   id="textarea"
                   v-model="text"
                   placeholder="Edición titulo..."
                   rows="3"
                   max-rows="6"
                   ></b-form-textarea>
				  
				  
				  <h7 class="text-primary p-2">
										Contenido
									</h7>
                  <b-form-textarea
                   id="textarea"
                   v-model="text"
                   placeholder="Edición contenido..."
                   rows="3"
                   max-rows="6"
                   ></b-form-textarea>
                  <pre class="mt-3 mb-0">{{ text }}</pre>
			
				
				<row>
						<b-col md="4">
				<h7 class="text-primary">
										#EJE
									</h7>
				</b-col>
				<b-col md="4">
				<div>
                <b-dropdown
                split
                split-variant="outline-primary"
                variant="primary"
                text="Ejes"
                class="m-2 "
                >
                <b-dropdown-item href="#">Bibliografia 1</b-dropdown-item>
                <b-dropdown-item href="#">Bibliografia 2</b-dropdown-item>
                <b-dropdown-item href="#">Bibliografia 3</b-dropdown-item>
                </b-dropdown>
                   </div>
				</b-col>
				<b-col md="4">
                <div class="buttonn">
				<b-button  squared lg="4" variant="primary">Agregar</b-button>
				</div>
				</b-col>
				</row>			
				<h7 class="text-primary p-1">
										#PAIS
									</h7>
				<h7 class="text-primary p-1">
										#ORGANISMO
									</h7>
				<h7 class="text-primary p-1">
										#PAIS
									</h7>	
				<h7 class="text-primary p-2">
										LINK
									</h7>
			
					
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
				<b-button  squared lg="4" variant="primary">Agregar</b-button>
				</div>
				<div class="buttonn p-4">
				<b-button  squared lg="4" variant="primary">Agregar</b-button>
				</div>
				<div class="buttonn p-4">
				<b-button  squared lg="4" variant="primary">Agregar</b-button>
				</div>
			
				
				   <div class="p-2">
			       <b-input-group >
                   <b-form-input></b-form-input>
                   <b-input-group-append>
                   <b-button variant="outline-success">Button</b-button>
                   </b-input-group-append>
                   </b-input-group>
                   </div>
				   <h7 class="text-primary p-2">
										BIBLIOGRAFIA
									</h7>
					 <div class="p-2">
			       <b-input-group >
                   <b-form-input></b-form-input>
                   <b-input-group-append>
                   <b-button variant="outline-success">Agregar</b-button>
                   </b-input-group-append>
                   </b-input-group>
                   </div>	
				    <div class="p-2">
			       <b-input-group >
                   <b-form-input></b-form-input>
                   <b-input-group-append>
                   <b-button variant="outline-success">Agregar</b-button>
                   </b-input-group-append>
                   </b-input-group>
                   </div>			
				
				
                  </div>
				</b-col>
			</b-row>
		</b-col>
	</b-row>


</b-container>
</template>>
<script>
export default {
    name: "vistaPrincipal"
}
</script>
<style scoped>

</style>>