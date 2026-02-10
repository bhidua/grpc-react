--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    book_id SERIAL PRIMARY KEY,
    name character varying(50) NOT NULL,
    author character varying(50) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_update timestamp without time zone,
    is_available boolean DEFAULT true NOT NULL
);

--
-- Name: library_book_transactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.library_book_transactions (
    transaction_id SERIAL PRIMARY KEY,
    book_id integer,
    member_id integer,
    borrowed_time timestamp without time zone NOT NULL,
    returned_time timestamp without time zone NOT NULL
);


--
-- Name: member; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.member (
    member_id SERIAL PRIMARY KEY,
    name character varying(50) NOT NULL,
    phone character varying(50) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_update timestamp without time zone
);

