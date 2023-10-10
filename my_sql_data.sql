select * from django_db_practice.ejercicioapp1_temporada;
select * from django_db_practice.ejercicioapp1_proveedor;


insert into django_db_practice.ejercicioapp1_temporada(id_temporada, nombre, descripcion) 
values (default, "Verano", "Altas temperaturas y aire libre");
insert into django_db_practice.ejercicioapp1_temporada(id_temporada, nombre, descripcion) 
values (default, "Invierno", "Bajas temperaturas y salud");

insert into django_db_practice.ejercicioapp1_proveedor(id_proveedor, nombre_empresa, pais_origen, contacto, tipo_colaboracion) 
values (default, "Nike", "EE.UU", "993 3344 223", "Ropa deportiva");
insert into django_db_practice.ejercicioapp1_proveedor(id_proveedor, nombre_empresa, pais_origen, contacto, tipo_colaboracion) 
values (default, "LaCoste", "EE.UU", "993 3344 223", "Ropa de todo tipo mayormente de temporada");


