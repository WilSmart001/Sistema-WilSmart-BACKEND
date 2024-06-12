/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     12/06/2024 0:41:51                           */
/*==============================================================*/


drop index CARGOS_PK;

drop table CARGOS;

drop index CATEGORIAS_PK;

drop table CATEGORIAS;

drop index CLIENTES_PK;

drop table CLIENTES;

drop index TIENE4_FK;

drop index ES2_FK;

drop index EMPLEADOS_PK;

drop table EMPLEADOS;

drop index ESTADOS_CIVILES_PK;

drop table ESTADOS_CIVILES;

drop index MARCAS_PK;

drop table MARCAS;

drop index ES3_FK;

drop index DE_FK;

drop index PRODUCTOS_PK;

drop table PRODUCTOS;

/*==============================================================*/
/* Table: CARGOS                                                */
/*==============================================================*/
create table CARGOS (
   COD_CARGOS           SERIAL               not null,
   NOMBRE_CAR           CHAR(50)             not null,
   constraint PK_CARGOS primary key (COD_CARGOS)
);

/*==============================================================*/
/* Index: CARGOS_PK                                             */
/*==============================================================*/
create unique index CARGOS_PK on CARGOS (
COD_CARGOS
);

/*==============================================================*/
/* Table: CATEGORIAS                                            */
/*==============================================================*/
create table CATEGORIAS (
   COD_CATEGORIAS       SERIAL               not null,
   NOMBRE_CAT           CHAR(40)             not null,
   constraint PK_CATEGORIAS primary key (COD_CATEGORIAS)
);

/*==============================================================*/
/* Index: CATEGORIAS_PK                                         */
/*==============================================================*/
create unique index CATEGORIAS_PK on CATEGORIAS (
COD_CATEGORIAS
);

/*==============================================================*/
/* Table: CLIENTES                                              */
/*==============================================================*/
create table CLIENTES (
   COD_CLIENTES         SERIAL               not null,
   NOMBRE_CLI           CHAR(40)             not null,
   IDENTIFICACION_CLI   CHAR(15)             not null,
   CELULAR_CLI          CHAR(8)              not null,
   CORREO_CLI           CHAR(150)            not null,
   DOMICILIO_CLI        CHAR(255)            not null,
   constraint PK_CLIENTES primary key (COD_CLIENTES)
);

/*==============================================================*/
/* Index: CLIENTES_PK                                           */
/*==============================================================*/
create unique index CLIENTES_PK on CLIENTES (
COD_CLIENTES
);

/*==============================================================*/
/* Table: EMPLEADOS                                             */
/*==============================================================*/
create table EMPLEADOS (
   COD_EMPLEADOS        SERIAL               not null,
   COD_ESTADOS_CIVILES  INT4                 not null,
   COD_CARGOS           INT4                 not null,
   NOMBRE_COMPLETO_EMP  CHAR(50)             not null,
   TELEFONO_EMP         CHAR(8)              not null,
   CI_EMP               CHAR(16)             not null,
   SALARIO_EMP          MONEY                not null,
   FOTO_EMP             CHAR(300)            not null,
   CORREO_EMP           CHAR(200)            not null,
   FECHA_NACIMIENTO_EMP DATE                 not null,
   DIRECCION_EMP        CHAR(300)            not null,
   constraint PK_EMPLEADOS primary key (COD_EMPLEADOS)
);

/*==============================================================*/
/* Index: EMPLEADOS_PK                                          */
/*==============================================================*/
create unique index EMPLEADOS_PK on EMPLEADOS (
COD_EMPLEADOS
);

/*==============================================================*/
/* Index: ES2_FK                                                */
/*==============================================================*/
create  index ES2_FK on EMPLEADOS (
COD_ESTADOS_CIVILES
);

/*==============================================================*/
/* Index: TIENE4_FK                                             */
/*==============================================================*/
create  index TIENE4_FK on EMPLEADOS (
COD_CARGOS
);

/*==============================================================*/
/* Table: ESTADOS_CIVILES                                       */
/*==============================================================*/
create table ESTADOS_CIVILES (
   COD_ESTADOS_CIVILES  SERIAL               not null,
   NOMBRE_EC            CHAR(50)             not null,
   constraint PK_ESTADOS_CIVILES primary key (COD_ESTADOS_CIVILES)
);

/*==============================================================*/
/* Index: ESTADOS_CIVILES_PK                                    */
/*==============================================================*/
create unique index ESTADOS_CIVILES_PK on ESTADOS_CIVILES (
COD_ESTADOS_CIVILES
);

/*==============================================================*/
/* Table: MARCAS                                                */
/*==============================================================*/
create table MARCAS (
   COD_MARCAS           SERIAL               not null,
   NOMBRE_MAR           CHAR(40)             not null,
   constraint PK_MARCAS primary key (COD_MARCAS)
);

/*==============================================================*/
/* Index: MARCAS_PK                                             */
/*==============================================================*/
create unique index MARCAS_PK on MARCAS (
COD_MARCAS
);

/*==============================================================*/
/* Table: PRODUCTOS                                             */
/*==============================================================*/
create table PRODUCTOS (
   COD_PRODUCTO         SERIAL               not null,
   COD_CATEGORIAS       INT4                 not null,
   COD_MARCAS           INT4                 not null,
   NOMBRE_PRO           CHAR(30)             not null,
   CANTIDAD_PRO         INT4                 not null,
   FECHA_PRO            DATE                 not null,
   PRECIO_PRO           MONEY                not null,
   IMAGEN_PRO           CHAR(400)            not null,
   DESCRIPCION_PRO      CHAR(500)            not null,
   constraint PK_PRODUCTOS primary key (COD_PRODUCTO)
);

/*==============================================================*/
/* Index: PRODUCTOS_PK                                          */
/*==============================================================*/
create unique index PRODUCTOS_PK on PRODUCTOS (
COD_PRODUCTO
);

/*==============================================================*/
/* Index: DE_FK                                                 */
/*==============================================================*/
create  index DE_FK on PRODUCTOS (
COD_MARCAS
);

/*==============================================================*/
/* Index: ES3_FK                                                */
/*==============================================================*/
create  index ES3_FK on PRODUCTOS (
COD_CATEGORIAS
);

alter table EMPLEADOS
   add constraint FK_EMPLEADO_ES2_ESTADOS_ foreign key (COD_ESTADOS_CIVILES)
      references ESTADOS_CIVILES (COD_ESTADOS_CIVILES)
      on delete restrict on update restrict;

alter table EMPLEADOS
   add constraint FK_EMPLEADO_TIENE4_CARGOS foreign key (COD_CARGOS)
      references CARGOS (COD_CARGOS)
      on delete restrict on update restrict;

alter table PRODUCTOS
   add constraint FK_PRODUCTO_DE_MARCAS foreign key (COD_MARCAS)
      references MARCAS (COD_MARCAS)
      on delete restrict on update restrict;

alter table PRODUCTOS
   add constraint FK_PRODUCTO_ES3_CATEGORI foreign key (COD_CATEGORIAS)
      references CATEGORIAS (COD_CATEGORIAS)
      on delete restrict on update restrict;

