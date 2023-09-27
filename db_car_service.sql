/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 15.1 		*/
/*  Created On : 14-sept.-2023 7:52:45 p. m. 				*/
/*  DBMS       : PostgreSQL 						*/
/* ---------------------------------------------------- */

/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS public.car_brand_id_seq
;

DROP SEQUENCE IF EXISTS public.car_model_id_seq
;

DROP SEQUENCE IF EXISTS public.service_id_seq
;

DROP SEQUENCE IF EXISTS public.spare_model_id_seq
;

DROP SEQUENCE IF EXISTS public.spare_service_id_seq
;

/* Drop Tables */

DROP TABLE IF EXISTS public.car_brand CASCADE
;

DROP TABLE IF EXISTS public.car_model CASCADE
;

DROP TABLE IF EXISTS public.service CASCADE
;

DROP TABLE IF EXISTS public.service_car_model CASCADE
;

DROP TABLE IF EXISTS public.spare_model CASCADE
;

DROP TABLE IF EXISTS public.spare_service CASCADE
;

/* Create Tables */

CREATE TABLE public.car_brand
(
	id bigint NOT NULL   DEFAULT NEXTVAL(('public."car_brand_id_seq"'::text)::regclass),
	name varchar(250) NULL,
	is_active boolean NULL
)
;

CREATE TABLE public.car_model
(
	id bigint NOT NULL   DEFAULT NEXTVAL(('public."car_model_id_seq"'::text)::regclass),
	name varchar(250) NULL,
	is_active boolean NULL,
	car_brand_id bigint NULL
)
;

CREATE TABLE public.service
(
	id bigint NOT NULL   DEFAULT NEXTVAL(('public."service_id_seq"'::text)::regclass),
	name varchar(250) NULL,
	is_active boolean NULL,
	spare_service_id bigint NULL
)
;

CREATE TABLE public.service_car_model
(
	service_id bigint NULL,
	car_model_id bigint NULL
)
;

CREATE TABLE public.spare_model
(
	id bigint NOT NULL   DEFAULT NEXTVAL(('public."spare_model_id_seq"'::text)::regclass),
	name varchar(250) NULL,
	is_active boolean NULL,
	car_model_id bigint NULL
)
;

CREATE TABLE public.spare_service
(
	id bigint NOT NULL   DEFAULT NEXTVAL(('public."spare_service_id_seq"'::text)::regclass),
	name varchar(250) NULL,
	is_active boolean NULL,
	spare_model_id bigint NULL
)
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE public.car_brand ADD CONSTRAINT "PK_car_brand"
	PRIMARY KEY (id)
;

ALTER TABLE public.car_model ADD CONSTRAINT "PK_car_model"
	PRIMARY KEY (id)
;

CREATE INDEX "IXFK_car_model_car_brand" ON public.car_model (car_brand_id ASC)
;

ALTER TABLE public.service ADD CONSTRAINT "PK_service"
	PRIMARY KEY (id)
;

CREATE INDEX "IXFK_service_spare_service" ON public.service (spare_service_id ASC)
;

CREATE INDEX "IXFK_service_car_model_car_model" ON public.service_car_model (car_model_id ASC)
;

CREATE INDEX "IXFK_service_car_model_service" ON public.service_car_model (service_id ASC)
;

ALTER TABLE public.spare_model ADD CONSTRAINT "PK_spare_model"
	PRIMARY KEY (id)
;

CREATE INDEX "IXFK_spare_model_car_model" ON public.spare_model (car_model_id ASC)
;

ALTER TABLE public.spare_service ADD CONSTRAINT "PK_spare_service"
	PRIMARY KEY (id)
;

CREATE INDEX "IXFK_spare_service_spare_model" ON public.spare_service (spare_model_id ASC)
;

/* Create Foreign Key Constraints */

ALTER TABLE public.car_model ADD CONSTRAINT "FK_car_model_car_brand"
	FOREIGN KEY (car_brand_id) REFERENCES public.car_brand (id) ON DELETE Restrict ON UPDATE Cascade
;

ALTER TABLE public.service ADD CONSTRAINT "FK_service_spare_service"
	FOREIGN KEY (spare_service_id) REFERENCES public.spare_service (id) ON DELETE Restrict ON UPDATE Cascade
;

ALTER TABLE public.service_car_model ADD CONSTRAINT "FK_service_car_model_car_model"
	FOREIGN KEY (car_model_id) REFERENCES public.car_model (id) ON DELETE Restrict ON UPDATE Cascade
;

ALTER TABLE public.service_car_model ADD CONSTRAINT "FK_service_car_model_service"
	FOREIGN KEY (service_id) REFERENCES public.service (id) ON DELETE Restrict ON UPDATE Cascade
;

ALTER TABLE public.spare_model ADD CONSTRAINT "FK_spare_model_car_model"
	FOREIGN KEY (car_model_id) REFERENCES public.car_model (id) ON DELETE Restrict ON UPDATE Cascade
;

ALTER TABLE public.spare_service ADD CONSTRAINT "FK_spare_service_spare_model"
	FOREIGN KEY (spare_model_id) REFERENCES public.spare_model (id) ON DELETE Restrict ON UPDATE Cascade
;

/* Create Table Comments, Sequences for Autonumber Columns */

CREATE SEQUENCE public.car_brand_id_seq INCREMENT 1 START 1
;

CREATE SEQUENCE public.car_model_id_seq INCREMENT 1 START 1
;

CREATE SEQUENCE public.service_id_seq INCREMENT 1 START 1
;

CREATE SEQUENCE public.spare_model_id_seq INCREMENT 1 START 1
;

CREATE SEQUENCE public.spare_service_id_seq INCREMENT 1 START 1
;
