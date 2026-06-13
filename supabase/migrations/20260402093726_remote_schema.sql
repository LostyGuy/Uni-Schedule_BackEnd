alter table "public"."schedules" drop constraint "schedules_group_id_fkey";

alter table "public"."schedules" drop column "group_id";

alter table "public"."schedules" add column "groupId" bigint;

alter table "public"."schedules" add constraint "schedules_groupId_fkey" FOREIGN KEY ("groupId") REFERENCES public.groups("groupId") ON UPDATE CASCADE ON DELETE RESTRICT not valid;

alter table "public"."schedules" validate constraint "schedules_groupId_fkey";


