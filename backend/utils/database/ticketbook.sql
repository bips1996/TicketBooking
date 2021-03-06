PGDMP         &    
            z         
   ticketbook    14.4    14.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            
           1262    16453 
   ticketbook    DATABASE     f   CREATE DATABASE ticketbook WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_India.1252';
    DROP DATABASE ticketbook;
                postgres    false            ?            1259    16476    movie_details    TABLE     ?   CREATE TABLE public.movie_details (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date timestamp without time zone NOT NULL
);
 !   DROP TABLE public.movie_details;
       public         heap    postgres    false            ?            1259    16475    movie_details_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.movie_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.movie_details_id_seq;
       public          postgres    false    212                       0    0    movie_details_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.movie_details_id_seq OWNED BY public.movie_details.id;
          public          postgres    false    211            ?            1259    16486    tickets    TABLE     ?   CREATE TABLE public.tickets (
    id integer NOT NULL,
    customer integer,
    movie integer,
    created_date timestamp without time zone,
    movie_time timestamp without time zone,
    ticket_price double precision,
    no_of_tickets integer
);
    DROP TABLE public.tickets;
       public         heap    postgres    false            ?            1259    16485    tickets_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.tickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.tickets_id_seq;
       public          postgres    false    214                       0    0    tickets_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.tickets_id_seq OWNED BY public.tickets.id;
          public          postgres    false    213            ?            1259    16466    user_details    TABLE     w   CREATE TABLE public.user_details (
    id integer NOT NULL,
    name character varying,
    email character varying
);
     DROP TABLE public.user_details;
       public         heap    postgres    false            ?            1259    16465    user_details_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.user_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.user_details_id_seq;
       public          postgres    false    210                       0    0    user_details_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.user_details_id_seq OWNED BY public.user_details.id;
          public          postgres    false    209            g           2604    16479    movie_details id    DEFAULT     t   ALTER TABLE ONLY public.movie_details ALTER COLUMN id SET DEFAULT nextval('public.movie_details_id_seq'::regclass);
 ?   ALTER TABLE public.movie_details ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    212    212            h           2604    16489 
   tickets id    DEFAULT     h   ALTER TABLE ONLY public.tickets ALTER COLUMN id SET DEFAULT nextval('public.tickets_id_seq'::regclass);
 9   ALTER TABLE public.tickets ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            f           2604    16469    user_details id    DEFAULT     r   ALTER TABLE ONLY public.user_details ALTER COLUMN id SET DEFAULT nextval('public.user_details_id_seq'::regclass);
 >   ALTER TABLE public.user_details ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210                      0    16476    movie_details 
   TABLE DATA           @   COPY public.movie_details (id, title, release_date) FROM stdin;
    public          postgres    false    212   ]                  0    16486    tickets 
   TABLE DATA           m   COPY public.tickets (id, customer, movie, created_date, movie_time, ticket_price, no_of_tickets) FROM stdin;
    public          postgres    false    214   ?!                  0    16466    user_details 
   TABLE DATA           7   COPY public.user_details (id, name, email) FROM stdin;
    public          postgres    false    210   x#                  0    0    movie_details_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.movie_details_id_seq', 22, true);
          public          postgres    false    211                       0    0    tickets_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.tickets_id_seq', 64, true);
          public          postgres    false    213                       0    0    user_details_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.user_details_id_seq', 7, true);
          public          postgres    false    209            n           2606    16483     movie_details movie_details_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.movie_details
    ADD CONSTRAINT movie_details_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.movie_details DROP CONSTRAINT movie_details_pkey;
       public            postgres    false    212            q           2606    16491    tickets tickets_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.tickets
    ADD CONSTRAINT tickets_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.tickets DROP CONSTRAINT tickets_pkey;
       public            postgres    false    214            k           2606    16473    user_details user_details_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.user_details DROP CONSTRAINT user_details_pkey;
       public            postgres    false    210            l           1259    16484    ix_movie_details_id    INDEX     K   CREATE INDEX ix_movie_details_id ON public.movie_details USING btree (id);
 '   DROP INDEX public.ix_movie_details_id;
       public            postgres    false    212            o           1259    16502    ix_tickets_id    INDEX     ?   CREATE INDEX ix_tickets_id ON public.tickets USING btree (id);
 !   DROP INDEX public.ix_tickets_id;
       public            postgres    false    214            i           1259    16474    ix_user_details_id    INDEX     I   CREATE INDEX ix_user_details_id ON public.user_details USING btree (id);
 &   DROP INDEX public.ix_user_details_id;
       public            postgres    false    210            r           2606    16492    tickets tickets_customer_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.tickets
    ADD CONSTRAINT tickets_customer_fkey FOREIGN KEY (customer) REFERENCES public.user_details(id);
 G   ALTER TABLE ONLY public.tickets DROP CONSTRAINT tickets_customer_fkey;
       public          postgres    false    214    3179    210            s           2606    16497    tickets tickets_movie_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.tickets
    ADD CONSTRAINT tickets_movie_fkey FOREIGN KEY (movie) REFERENCES public.movie_details(id);
 D   ALTER TABLE ONLY public.tickets DROP CONSTRAINT tickets_movie_fkey;
       public          postgres    false    3182    212    214               N  x?u?Mn?0F??s?D??	aEJR??&???f?0v?8Pn_?B?B?????olF???P?&?r??ɂS?,?I?e?A?YM?????N??l??Pj????3B????`?]??br*???T
??V??r?????S`5`!?\??\???O?᮪?*????le#?8??a??2?'?????ԵԅW`??W?7????A?3???I????u?D|A??d?ݸ??h$ u?????Ջ?dG?KԷ?D????ˠ1??|???p???:???3'}??m#?\?gSɡ?>%/Fk-??yFv???'?7???p4*?b\H<?89`[?N???e?ML??         ?  x???Mr?0??}?^ K?9K???i??^??,?x??A<?? ?Ӥ?H???C?????g??;.?MS?X??V?f??L?
m{???-l?Z?$e%J??eZh???NY?xl~??Iu??g/????6b???.??ߪ??>???u??`4FDy??????a?j??8G?kT?"?:?c???oA???Q??7/?%Zr|?K?]?9r~??p78?fy??????o\_???tWy?և?]?mJw???[NC?.cD??????q?1?a?q?1??~L?4??c/9???׌W ?????X???? a4????%-+?h?i??ֆ????#txr6Ţ??uu??W ???:r*{???4??c|??M??J?=+??7??c??oǆ^?Y???)|H;???ۻ?ǖ^?7ҾĊF[?9//|^{??????c?8М*          s   x?M̻?@D?z?c?³4AJIK???`	????m\??j??N??<?ˮ?9????\?^?I1????g
Фi%??Q?KҴ
?g??%M?????/??)M\???խic???=?A?     