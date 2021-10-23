-- Adminer 4.8.1 PostgreSQL 13.4 (Debian 13.4-4.pgdg110+1) dump

DROP TABLE IF EXISTS "venicle";
DROP SEQUENCE IF EXISTS venicle_id_seq;
CREATE SEQUENCE venicle_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."venicle" (
    "id" integer DEFAULT nextval('venicle_id_seq') NOT NULL,
    "name" character varying(20) NOT NULL,
    "number" character varying(10) NOT NULL,
    "coord" double precision[],
    CONSTRAINT "ix_venicle_name" UNIQUE ("name"),
    CONSTRAINT "venicle_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_venicle_id" ON "public"."venicle" USING btree ("id");

INSERT INTO "venicle" ("id", "name", "number", "coord") VALUES
(1,	'Машина 1',	'o000oo',	'{52.60409007851464,39.53793764131006}'),
(2,	'Машина 2',	'o001oo',	'{52.605758098557764,39.53278887744928}'),
(3,	'Машина 3',	'o003oo',	'{52.609198189273584,39.5296996191328}')
(4,	'Машина 4',	'o004oo',	'{52.60409007851464,39.53793764131006}'),
(5,	'Машина 5',	'o005oo',	'{52.605758098557764,39.53278887744928}'),
(6,	'Машина 6',	'o006oo',	'{52.609198189273584,39.5296996191328}'),
(7,	'Машина 7',	'o007oo',	'{52.60409007851464,39.53793764131006}'),
(8,	'Машина 8',	'o008oo',	'{52.605758098557764,39.53278887744928}'),
(9,	'Машина 9',	'o009oo',	'{52.609198189273584,39.5296996191328}'),
(10,'Машина 10',	'o010oo',	'{52.60409007851464,39.53793764131006}'),
(11,'Машина 11',	'o011oo',	'{52.605758098557764,39.53278887744928}'),
(12,'Машина 12',	'o012oo',	'{52.609198189273584,39.5296996191328}'),
(13,'Машина 13',	'o013oo',	'{52.60409007851464,39.53793764131006}'),
(14,'Машина 14',	'o014oo',	'{52.605758098557764,39.53278887744928}'),
(15,'Машина 15',	'o015oo',	'{52.609198189273584,39.5296996191328}');

-- 2021-10-23 10:18:42.537737+00