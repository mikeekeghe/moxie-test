CREATE SCHEMA IF NOT EXISTS public;

CREATE TYPE public.status_type_enum AS ENUM('Scheduled', 'Completed', 'Canceled');

CREATE TABLE public.appointment(
  id SERIAL PRIMARY KEY,
  start_time timestamp NOT NULL,
  total_duration integer NOT NULL,
  total_price integer NOT NULL,
  status status_type_enum NOT NULL,
  medspa_id integer NOT NULL
);

CREATE TABLE public.medspa(
  id SERIAL PRIMARY KEY,
  name varchar NOT NULL,
  address varchar NOT NULL,
  phone_number varchar,
  email varchar
);

CREATE TABLE public.service(
  id SERIAL PRIMARY KEY,
  name varchar NOT NULL,
  description varchar,
  price varchar NOT NULL,
  duration varchar NOT NULL,
  medspa_id integer NOT NULL,
  appointment_id integer NOT NULL
);

ALTER TABLE public.appointment
  ADD CONSTRAINT appointment_medspa_id_fkey
    FOREIGN KEY (medspa_id) REFERENCES public.medspa (id);

ALTER TABLE public.service
  ADD CONSTRAINT service_medspa_id_fkey
    FOREIGN KEY (medspa_id) REFERENCES public.medspa (id);

ALTER TABLE public.service
  ADD CONSTRAINT service_appointment_id_fkey
    FOREIGN KEY (appointment_id) REFERENCES public.appointment (id);

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
