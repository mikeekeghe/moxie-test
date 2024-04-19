SET check_function_bodies = false
;

CREATE TYPE status_type_enum AS ENUM(Scheduled
Completed
Canceled);

CREATE TABLE appointment(
  id integer NOT NULL,
  start_time timestamp NOT NULL,
  total_duration integer NOT NULL,
  total_price integer NOT NULL,
  status status_type_enum NOT NULL,
  medspa_id integer NOT NULL,
  CONSTRAINT appointment_pkey PRIMARY KEY(id)
);

CREATE TABLE medspa(
  id integer NOT NULL,
  "name" varchar NOT NULL,
  address varchar NOT NULL,
  phone_number varchar,
  email varchar,
  CONSTRAINT medspa_pkey PRIMARY KEY(id)
);

CREATE TABLE service(
  id integer NOT NULL,
  "name" varchar NOT NULL,
  description varchar,
  price varchar NOT NULL,
  duration varchar NOT NULL,
  medspa_id integer NOT NULL,
  appointment_id integer NOT NULL,
  CONSTRAINT service_pkey PRIMARY KEY(id)
);

ALTER TABLE appointment
  ADD CONSTRAINT appointment_medspa_id_fkey
    FOREIGN KEY (medspa_id) REFERENCES medspa (id);

ALTER TABLE service
  ADD CONSTRAINT service_medspa_id_fkey
    FOREIGN KEY (medspa_id) REFERENCES medspa (id);

ALTER TABLE service
  ADD CONSTRAINT service_appointment_id_fkey
    FOREIGN KEY (appointment_id) REFERENCES appointment (id);
