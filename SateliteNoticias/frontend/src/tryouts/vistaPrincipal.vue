<template>
    <b-container class="bv-example-row">
     <b-row>
	        <b-col md="8">
					<h3 class="text-center">
						Satelite de Noticias 
					</h3>
				</b-col>
		    <b-col md="4">
					<b-row>
						<b-col md="6">
							 
							<b-button variant="success">Configuración</b-button>
						</b-col>
						<b-col md="6">
							 
							<b-button variant="success">Usuario</b-button>
						</b-col>
					</b-row>
				</b-col>
	</b-row>

	<b-row>
		<b-col md="12">
		
			<b-row>
				<b-col md="3">
					    <div class="dropdown">
						 
						               <b-dropdown class="mx-1" right text="Categorias">
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
							 
							            <b-button variant="success">Trending</b-button>
						          </b-col>
						        <b-col md="4">
						        </b-col>
						          <b-col md="4">
							 
							            <b-button variant="success">Buscar</b-button>
						           </b-col>
					        </b-row>
                        
			        <b-row>
						<b-col md="12">
							<b-row>
								<b-col md="12">
									   <b-jumbotron header="Titulo Noticias" lead="Link:www.páginawb.cl">
										 <p>Resumen Noticias</p>
										     <b-button variant="primary" href="#">Seguir leyendo</b-button>
                                       </b-jumbotron>
								</b-col>
						    </b-row>
							
					<b-row>
                    
						<b-col md="12">
                                    
									 <h7 class="text-right">
										  #Visitas=200
									  </h7>
						</b-col>
					</b-row>
		                <b-row>
							<b-col md="3">
									<div class="dropdown">
										 
										      <b-dropdown class="mx-1" right text="#EJE">
                                              <b-dropdown-item>Eje 1</b-dropdown-item>
                                              <b-dropdown-item>Eje 2</b-dropdown-item>
                                              <b-dropdown-item>Eje 3</b-dropdown-item>
                                              </b-dropdown>
										   <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
											 <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
										    </div>
									</div>
							</b-col>
								<b-col md="3">
									<div class="dropdown">
									       <b-dropdown class="mx-1" right text="#PAIS">
                                           <b-dropdown-item>Pais 1 </b-dropdown-item>
                                           <b-dropdown-item>Pais 2</b-dropdown-item>
                                           <b-dropdown-item>Pais 3</b-dropdown-item>	
                                            </b-dropdown> 
									
										    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
											  <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
										    </div>
									</div>
								</b-col>
								<b-col md="3">
									<div class="dropdown">
										    <b-dropdown class="mx-1" right text="#ORGANISMO">
                                            <b-dropdown-item>Organismo 1 </b-dropdown-item>
                                            <b-dropdown-item>Organismo 2</b-dropdown-item>
                                            <b-dropdown-item>Organismo 3</b-dropdown-item>	
                                            </b-dropdown>
							
										   <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
											 <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
										  </div>
									</div>
								</b-col>
								<b-col md="3">
									<div class="dropdown">
										 
										   <b-dropdown class="mx-1" right text="#FECHA">
                                           <b-dropdown-item>Fecha 1 </b-dropdown-item>
                                           <b-dropdown-item>Fecha 2</b-dropdown-item>
                                           <b-dropdown-item>Fecha 3</b-dropdown-item>	
                                           </b-dropdown>
										<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
											 <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
										</div>
									</div>
								</b-col>
						</b-row>
							<b-row>
								<b-col md="12">
								</b-col>
							</b-row>
							<b-row>
								<b-col md="3">
									<h7>
										BIBLIOGRAFIA
									</h7>
								</b-col>
								<b-col md="3">
									<div class="dropdown">
										 
										   <b-dropdown class="mx-1" right text="Nombre">
                                           <b-dropdown-item>Nombre Bibliografia 1 </b-dropdown-item>
                                           <b-dropdown-item>Nombre Bibliografia 2</b-dropdown-item>
                                           <b-dropdown-item>Nombre Bibliografia 3</b-dropdown-item>	
                                           </b-dropdown> 
                                           
										<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
											 <a class="dropdown-item disabled" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a>
										</div>
									 </div>
								</b-col>
								    <b-col md="3">
                                        <b-input-group size="sm" prepend="link" >
                                            <b-form-input value=" " class="text-right"></b-form-input>
                                           </b-input-group>
								    </b-col>
								         <b-col md="3">
								         </b-col>
							</b-row>
							<b-row>
								<b-col md="6">
								</b-col>
								     <b-col md="6">
									    <b-button variant="success">Editar</b-button>
								     </b-col>
							</b-row>
						
							  
				     </b-col>
			        </b-row>
		            </b-col>
				<b-col md="2">
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