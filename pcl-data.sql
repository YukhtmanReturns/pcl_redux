

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;



--
-- Users
--

INSERT INTO pcl_user VALUES (1, 'ohardt@gmail.com', 'Oliver', '36c2fbf9ee46f95e28c8b17107529628', '542698d72c12c1f149d6f50692c75ea6', '6aca6c8e7584d48d77cb02dd0079f167', 'M', 'U', '1978-04-05', 10011, 0, 0, true, true);

INSERT INTO pcl_user VALUES (2, 'christok69@gmail.com', NULL, '85d87b1a3266f7064f0881d1df36fe5a', '6bab4bd46a68576fa5782b5672753beb', '61ff096e5f36a7a2364370f97e5eb896', ' ', 'U', NULL, NULL, 0, 0, false, true);
INSERT INTO pcl_user VALUES (3, 'josh@gmail.com', NULL, '1fc058dbfb95afbb3dcf3a98c9bad831', '547a3b64c29a212e536def659cff5a4b', '64291a62a8ed709d89c45cac4c50df47', ' ', 'U', NULL, NULL, 0, 0, false, true);
INSERT INTO pcl_user VALUES (6, 'christok69_1@gmail.com', NULL, '0c37b73753ef8c0e0ae08431f2d77b84', '1d51edd131c257f557da0e1309bbb1cd', 'f357c853ec92a8bb04db24779322bfaf', ' ', 'U', NULL, NULL, 0, 0, false, true);
INSERT INTO pcl_user VALUES (7, 'christok@gmail.com', NULL, '4742a6b241660ad12686d5d9dad2b9df', 'bd105fb5c0cefe9967db962913eaf24b', '220b5d26603ecb4bb3e8d8caa32a6993', ' ', 'U', NULL, NULL, 0, 0, false, true);
INSERT INTO pcl_user VALUES (8, 'jrphoner@hotmail.com', NULL, '8a11e183458be6dba75145f96a6e6a28', '957316ec03dda30d77776947c44838f5', 'b071bf792e1466411300cac704ad02af', ' ', 'U', NULL, NULL, 0, 0, false, true);


INSERT INTO pcl_user VALUES (9, 'test1@21zoo.com', NULL, '27facdc3afc1b8fcc9c04739c247f801', '9962fcb2b19cd71a5268700cd7b9bda3', '085d0c4b8289d482f81e05c9ced1d8a9', ' ', 'U', NULL, NULL, 1372113590, 1372113590, false, true);
INSERT INTO pcl_user VALUES (10, 'test2@21zoo.com', NULL, 'b01cbe140d45422caceb23b88e0ed38b', 'ccd18ba64811eed85fde7b6def8d2177', '224ac84465874bfa87bd1a884053d6ab', ' ', 'U', NULL, NULL, 1372113608, 1372113608, false, true);
INSERT INTO pcl_user VALUES (11, 'test3@21zoo.com', NULL, '39e08a2dbe2aa022b7bd8e6cc0adbcbe', '26c0f3362f8650962896d711711679ce', '0cb56c8966d6c8c9c260ee9b71e2c989', ' ', 'U', NULL, NULL, 1372113633, 1372113633, false, true);
INSERT INTO pcl_user VALUES (13, 'test4@21zoo.com', NULL, '0b3a1c27da30047d8ce4fae6ae771b64', 'a5dbfdc905d75f702f288f13a355c4e1', '40c73b9db10c3b0d74d6c11a218d6c1e', ' ', 'U', NULL, NULL, 1372113669, 1372113669, false, true);
INSERT INTO pcl_user VALUES (14, 'test5@21zoo.com', NULL, '90be0f628670ccd40c43957e2e532a96', 'd9e256f456ddcb33447569e6b736be89', '74628270e627edfecdd669a5ebf64b01', ' ', 'U', NULL, NULL, 1372113688, 1372113688, false, true);

SELECT pg_catalog.setval('pcl_user_id_seq', 14, true);






--
-- Data for Name: pcl_contact; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_contact VALUES (1, 'blub blub', 1370898363, 1);
INSERT INTO pcl_contact VALUES (2, 'blub blubddsa ', 1370898375, 1);


--
-- Name: pcl_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('pcl_contact_id_seq', 2, true);


--
-- Data for Name: pcl_procedure; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_procedure VALUES (3, 'Open Heart Surgery', false, 'That really sucks');
INSERT INTO pcl_procedure VALUES (2, 'Root Canal', true, 'blub bla blub');
INSERT INTO pcl_procedure VALUES (5, 'Colonoscopy', true, 'http://www.facs.org/public_info/operation/brochures/colonoscopy.pdf');
INSERT INTO pcl_procedure VALUES (6, 'Upper GI Endoscopy', true, 'http://digestive.niddk.nih.gov/ddiseases/pubs/upperendoscopy/index.aspx');
INSERT INTO pcl_procedure VALUES (1, 'Wisdom Tooth Extraction', true, 'blub bla');
INSERT INTO pcl_procedure VALUES (7, 'Breast Biopsy', true, '( . ) ( . )');
INSERT INTO pcl_procedure VALUES (8, 'Lasik', true, 'http://www.geteyesmart.org/eyesmart/glasses-contacts-lasik/lasik.cfm');

SELECT pg_catalog.setval('pcl_procedure_id_seq', 8, true);


--
-- Data for Name: pcl_question; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_question VALUES (1, 'Why should I have my wisdom teeth removed?', FALSE, '', True);
INSERT INTO pcl_question VALUES (2, 'What are the chances that the teeth will grow in normally?', FALSE, '', True);
INSERT INTO pcl_question VALUES (3, 'Could I do watchful waiting with my dentist and get the surgery if I have pain?', FALSE, '', True);
INSERT INTO pcl_question VALUES (4, 'What precautions should I take if I decide to keep the wisdom teeth?', FALSE, '', True);
INSERT INTO pcl_question VALUES (5, 'What type of anesthesia do you use? Can I have local instead of general?', FALSE, '', True);
INSERT INTO pcl_question VALUES (6, 'What happens during wisdom teeth surgery?', FALSE, '', True);
INSERT INTO pcl_question VALUES (7, 'How much pain and swelling occurs after the wisdom tooth removal? How do I minimize it?', FALSE, '', True);
INSERT INTO pcl_question VALUES (8, 'How do I treat bleeding and pain after the wisdom tooth surgery?', FALSE, '', True);
INSERT INTO pcl_question VALUES (9, 'What can I eat or drink after wisdom tooth removal?', FALSE, '', True);
INSERT INTO pcl_question VALUES (10, 'When do I follow-up to get the stitches removed?', FALSE, '', True);
INSERT INTO pcl_question VALUES (11, 'Root Canal Q1', FALSE, '', True);
INSERT INTO pcl_question VALUES (12, 'Root Canal Q2', FALSE, '', True);
INSERT INTO pcl_question VALUES (13, 'Root Canal Q3', FALSE, '', True);
INSERT INTO pcl_question VALUES (14, 'Root Canal Q4', FALSE, '', True);
INSERT INTO pcl_question VALUES (15, 'blub', false, '', True);
INSERT INTO pcl_question VALUES (16, 'blub', false, '', True);
INSERT INTO pcl_question VALUES (17, 'blub', false, '', True);
INSERT INTO pcl_question VALUES (18, 'blub', false, '', True);
INSERT INTO pcl_question VALUES (19, 'blub', false, '', True);
INSERT INTO pcl_question VALUES (20, 'Moar Root', false, '', True);
INSERT INTO pcl_question VALUES (21, 'mooooooooooooo', false, '', True);
INSERT INTO pcl_question VALUES (22, 'warum', false, '', True);
INSERT INTO pcl_question VALUES (23, 'bitte', false, '', True);
INSERT INTO pcl_question VALUES (24, 'xxx', false, '', True);
INSERT INTO pcl_question VALUES (25, 'last', false, '', True);
INSERT INTO pcl_question VALUES (26, 'new last', false, '', True);
INSERT INTO pcl_question VALUES (27, 'new last', false, '', True);
INSERT INTO pcl_question VALUES (28, 'new ', false, '', True);
INSERT INTO pcl_question VALUES (33, 'What is the reason to do the test - to screen for colon cancer or to look for a cause of bleeding?', false, '', True);
INSERT INTO pcl_question VALUES (34, 'Could I do a flexible sigmoidoscopy, CT colonography, barium enema, stool blood test, or DNA stool test instead?', false, '', True);
INSERT INTO pcl_question VALUES (35, 'What is involved in the bowel prep before the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (36, 'How much pain and cramping can I expect during and after the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (37, 'Is there any risk of perforation or other serious consequences from the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (38, 'If a polyp is found what does that mean? What are the chances that it will be cancerous?', false, '', True);
INSERT INTO pcl_question VALUES (39, 'What will happen if you have to do a biopsy?', false, '', True);
INSERT INTO pcl_question VALUES (40, 'What sedatives and other medications will I be given during the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (41, 'Are there any possible heart and lung complications from the medicines given during the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (42, 'How soon can I drive, eat, and drink after the colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (43, 'When can I return to work after colonoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (44, 'Why am I getting an endoscopy - to look for a cause of bleeding, persistent heartburn, ulcers, or screen for cancer?', false, '', True);
INSERT INTO pcl_question VALUES (45, 'Could I just continue medications or get a CT scan, abdominal ultrasound, barium swallow, or other non-invasive test?', false, '', True);
INSERT INTO pcl_question VALUES (46, 'Will this endoscopy change my management? Will I be on the same medications as before?', false, '', True);
INSERT INTO pcl_question VALUES (47, 'What prep do I have to do for the endoscopy? What medications do I have to stop beforehand?', false, '', True);
INSERT INTO pcl_question VALUES (48, 'Will I be awake during the endoscopy? Will I have pain during the procedure?', false, '', True);
INSERT INTO pcl_question VALUES (49, 'What are the risks of bleeding or perforation from endoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (50, 'What are the side effects of the sedative, mouth spray, and other medications used during the endoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (51, 'When would you do a biopsy?', false, '', True);
INSERT INTO pcl_question VALUES (52, 'How long can I expect to have sore throat, bloating, or cramping after the endoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (53, 'How soon can I drive, eat, and drink after the endoscopy?', false, '', True);
INSERT INTO pcl_question VALUES (54, 'When can I resume normal activity after wisdom tooth extraction?', false, '', True);
INSERT INTO pcl_question VALUES (55, 'How do clean my mouth after the surgery? Can I brush?', false, '', True);
INSERT INTO pcl_question VALUES (56, 'How do I handle fever, numbness, nausea, or color changes in my face?', false, '', True);
INSERT INTO pcl_question VALUES (57, 'What are the chances that my lump may be cancerous? ', false, '', True);
INSERT INTO pcl_question VALUES (58, 'Do I need to have a biopsy? Could I do repeat mammograms, ultrasounds, or MRI tests instead?', false, '', True);
INSERT INTO pcl_question VALUES (59, 'Will I be having a surgical, fine-needle, stereotactic, or core needle biopsy? What does it entail?', false, '', True);
INSERT INTO pcl_question VALUES (60, 'Could I do a fine-needle biopsy instead?', false, '', True);
INSERT INTO pcl_question VALUES (61, 'What are the chances that the biopsy could miss cancer?', false, '', True);
INSERT INTO pcl_question VALUES (62, 'Is the biopsy procedure painful?', false, '', True);
INSERT INTO pcl_question VALUES (63, 'How common are bleeding, bruising, and infection after a biopsy?', false, '', True);
INSERT INTO pcl_question VALUES (64, 'Will the biopsy alter the appearance of my breast?', false, '', True);
INSERT INTO pcl_question VALUES (65, 'If my biopsy is benign, what type of follow-up will I need?', false, '', True);
INSERT INTO pcl_question VALUES (66, 'If my biopsy shows cancer, what would be the next steps?', false, '', True);
INSERT INTO pcl_question VALUES (67, 'When will I receive my biopsy results?', false, '', True);
INSERT INTO pcl_question VALUES (68, 'Is LASIK the right procedure for me? Would Radial Keratotomy (RK) or Photorefractive Keratectomy (PRK) be a better choice for me?', false, '', True);
INSERT INTO pcl_question VALUES (69, 'Am I too old to have Lasik? Will I still need reading glasses?', false, '', True);
INSERT INTO pcl_question VALUES (70, 'What are the chances that I will have full correction? ', false, '', True);
INSERT INTO pcl_question VALUES (71, 'How many patients need a repeat treatment?', false, '', True);
INSERT INTO pcl_question VALUES (72, 'What are the risks of halos, glare, and reduced nighttime vision?', false, '', True);
INSERT INTO pcl_question VALUES (73, 'What is the risk of vision loss?', false, '', True);
INSERT INTO pcl_question VALUES (74, 'Before the procedure, when should I stop wearing contacts and using makeup/creams on the face?', false, '', True);
INSERT INTO pcl_question VALUES (75, 'What do I have to do during the procedure? What if I blink or move during it?', false, '', True);
INSERT INTO pcl_question VALUES (76, 'What activities should I avoid after the surgery? ', false, '', True);
INSERT INTO pcl_question VALUES (77, 'How long I have to wear an eye shield?', false, '', True);
INSERT INTO pcl_question VALUES (78, 'What vision problems and discomfort will I have after the surgery?', false, '', True);
INSERT INTO pcl_question VALUES (79, 'How soon after Lasik will I be able to see clearly?', false, '', True);
INSERT INTO pcl_question VALUES (80, 'How many eyes has your doctor performed LASIK surgery on with the same type of laser?', false, '', True);
INSERT INTO pcl_question VALUES (81, 'Do you use an FDA-approved laser for the procedure? ', false, '', True);
INSERT INTO pcl_question VALUES (82, 'Does you use each microkeratome blade only once?', false, '', True);


SELECT pg_catalog.setval('pcl_question_id_seq', 82, true);


--
-- Data for Name: pcl_userlist; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_userlist VALUES (1, 'Root Canal List', 1371155823, true, 'e7c23a3bface11b23fade7fa0021aae7');
INSERT INTO pcl_userlist VALUES (2, 'My Wisdom Tooth List', 1371157966, true, 'a9868f265b7d76d9ed09659e90d9384c');
INSERT INTO pcl_userlist VALUES (3, 'new List', 1371186967, true, '2329ffb7875655592116136defeb95c9');

SELECT pg_catalog.setval('pcl_userlist_id_seq', 3, true);




INSERT INTO pcl_user_lists VALUES (1, 1, 1);
INSERT INTO pcl_user_lists VALUES (2, 1, 2);
INSERT INTO pcl_user_lists VALUES (3, 1, 3);


--
-- Name: pcl_user_lists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('pcl_user_lists_id_seq', 3, true);





--
-- Data for Name: pcl_listquestionorder; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_listquestionorder VALUES (5, 1, 8, 50000);
INSERT INTO pcl_listquestionorder VALUES (6, 1, 9, 60000);
INSERT INTO pcl_listquestionorder VALUES (7, 1, 10, 70000);
INSERT INTO pcl_listquestionorder VALUES (14, 1, 17, 90000);
INSERT INTO pcl_listquestionorder VALUES (16, 1, 19, 110000);
INSERT INTO pcl_listquestionorder VALUES (18, 2, 2, 20000);
INSERT INTO pcl_listquestionorder VALUES (20, 2, 4, 40000);
INSERT INTO pcl_listquestionorder VALUES (21, 2, 5, 50000);
INSERT INTO pcl_listquestionorder VALUES (22, 2, 6, 60000);
INSERT INTO pcl_listquestionorder VALUES (23, 2, 7, 70000);
INSERT INTO pcl_listquestionorder VALUES (26, 2, 10, 100000);
INSERT INTO pcl_listquestionorder VALUES (27, 1, 20, 120000);
INSERT INTO pcl_listquestionorder VALUES (28, 2, 21, 110000);
INSERT INTO pcl_listquestionorder VALUES (30, 2, 23, 130000);
INSERT INTO pcl_listquestionorder VALUES (36, 3, 2, 10000);
INSERT INTO pcl_listquestionorder VALUES (37, 3, 3, 20000);
INSERT INTO pcl_listquestionorder VALUES (38, 3, 5, 30000);
INSERT INTO pcl_listquestionorder VALUES (39, 3, 6, 40000);
INSERT INTO pcl_listquestionorder VALUES (40, 3, 8, 50000);
INSERT INTO pcl_listquestionorder VALUES (41, 3, 9, 60000);
INSERT INTO pcl_listquestionorder VALUES (42, 3, 10, 70000);
INSERT INTO pcl_listquestionorder VALUES (43, 3, 11, 80000);
INSERT INTO pcl_listquestionorder VALUES (44, 3, 12, 90000);
INSERT INTO pcl_listquestionorder VALUES (45, 3, 13, 100000);
INSERT INTO pcl_listquestionorder VALUES (46, 3, 14, 110000);


--
-- Name: pcl_listquestionorder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('pcl_listquestionorder_id_seq', 46, true);


--
-- Data for Name: pcl_procedure_questions; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_procedure_questions VALUES (12, 2, 2);
INSERT INTO pcl_procedure_questions VALUES (13, 2, 3);
INSERT INTO pcl_procedure_questions VALUES (15, 2, 5);
INSERT INTO pcl_procedure_questions VALUES (16, 2, 6);
INSERT INTO pcl_procedure_questions VALUES (18, 2, 8);
INSERT INTO pcl_procedure_questions VALUES (19, 2, 9);
INSERT INTO pcl_procedure_questions VALUES (20, 2, 10);
INSERT INTO pcl_procedure_questions VALUES (21, 2, 11);
INSERT INTO pcl_procedure_questions VALUES (22, 2, 12);
INSERT INTO pcl_procedure_questions VALUES (23, 2, 13);
INSERT INTO pcl_procedure_questions VALUES (24, 2, 14);
INSERT INTO pcl_procedure_questions VALUES (28, 5, 33);
INSERT INTO pcl_procedure_questions VALUES (29, 5, 34);
INSERT INTO pcl_procedure_questions VALUES (30, 5, 35);
INSERT INTO pcl_procedure_questions VALUES (31, 5, 36);
INSERT INTO pcl_procedure_questions VALUES (32, 5, 37);
INSERT INTO pcl_procedure_questions VALUES (33, 5, 38);
INSERT INTO pcl_procedure_questions VALUES (34, 5, 39);
INSERT INTO pcl_procedure_questions VALUES (35, 5, 40);
INSERT INTO pcl_procedure_questions VALUES (36, 5, 41);
INSERT INTO pcl_procedure_questions VALUES (37, 5, 42);
INSERT INTO pcl_procedure_questions VALUES (38, 5, 43);
INSERT INTO pcl_procedure_questions VALUES (39, 6, 44);
INSERT INTO pcl_procedure_questions VALUES (40, 6, 45);
INSERT INTO pcl_procedure_questions VALUES (41, 6, 46);
INSERT INTO pcl_procedure_questions VALUES (42, 6, 47);
INSERT INTO pcl_procedure_questions VALUES (43, 6, 48);
INSERT INTO pcl_procedure_questions VALUES (44, 6, 49);
INSERT INTO pcl_procedure_questions VALUES (45, 6, 50);
INSERT INTO pcl_procedure_questions VALUES (46, 6, 51);
INSERT INTO pcl_procedure_questions VALUES (47, 6, 52);
INSERT INTO pcl_procedure_questions VALUES (48, 6, 53);
INSERT INTO pcl_procedure_questions VALUES (49, 1, 1);
INSERT INTO pcl_procedure_questions VALUES (50, 1, 2);
INSERT INTO pcl_procedure_questions VALUES (51, 1, 3);
INSERT INTO pcl_procedure_questions VALUES (52, 1, 4);
INSERT INTO pcl_procedure_questions VALUES (53, 1, 5);
INSERT INTO pcl_procedure_questions VALUES (54, 1, 6);
INSERT INTO pcl_procedure_questions VALUES (55, 1, 7);
INSERT INTO pcl_procedure_questions VALUES (56, 1, 8);
INSERT INTO pcl_procedure_questions VALUES (57, 1, 9);
INSERT INTO pcl_procedure_questions VALUES (58, 1, 10);
INSERT INTO pcl_procedure_questions VALUES (59, 1, 54);
INSERT INTO pcl_procedure_questions VALUES (60, 1, 55);
INSERT INTO pcl_procedure_questions VALUES (61, 1, 56);
INSERT INTO pcl_procedure_questions VALUES (62, 7, 64);
INSERT INTO pcl_procedure_questions VALUES (63, 7, 65);
INSERT INTO pcl_procedure_questions VALUES (64, 7, 66);
INSERT INTO pcl_procedure_questions VALUES (65, 7, 67);
INSERT INTO pcl_procedure_questions VALUES (66, 7, 57);
INSERT INTO pcl_procedure_questions VALUES (67, 7, 58);
INSERT INTO pcl_procedure_questions VALUES (68, 7, 59);
INSERT INTO pcl_procedure_questions VALUES (69, 7, 60);
INSERT INTO pcl_procedure_questions VALUES (70, 7, 61);
INSERT INTO pcl_procedure_questions VALUES (71, 7, 62);
INSERT INTO pcl_procedure_questions VALUES (72, 7, 63);
INSERT INTO pcl_procedure_questions VALUES (73, 8, 68);
INSERT INTO pcl_procedure_questions VALUES (74, 8, 69);
INSERT INTO pcl_procedure_questions VALUES (75, 8, 70);
INSERT INTO pcl_procedure_questions VALUES (76, 8, 71);
INSERT INTO pcl_procedure_questions VALUES (77, 8, 72);
INSERT INTO pcl_procedure_questions VALUES (78, 8, 73);
INSERT INTO pcl_procedure_questions VALUES (79, 8, 74);
INSERT INTO pcl_procedure_questions VALUES (80, 8, 75);
INSERT INTO pcl_procedure_questions VALUES (81, 8, 76);
INSERT INTO pcl_procedure_questions VALUES (82, 8, 77);
INSERT INTO pcl_procedure_questions VALUES (83, 8, 78);
INSERT INTO pcl_procedure_questions VALUES (84, 8, 79);
INSERT INTO pcl_procedure_questions VALUES (85, 8, 80);
INSERT INTO pcl_procedure_questions VALUES (86, 8, 81);
INSERT INTO pcl_procedure_questions VALUES (87, 8, 82);


SELECT pg_catalog.setval('pcl_procedure_questions_id_seq', 87, true);






--
-- Data for Name: pcl_tag; Type: TABLE DATA; Schema: public; Owner: dbuser
--

INSERT INTO pcl_tag VALUES (1, 'tooth');
INSERT INTO pcl_tag VALUES (2, 'dentist');
INSERT INTO pcl_tag VALUES (3, 'wisdom');
INSERT INTO pcl_tag VALUES (4, 'extraction');
INSERT INTO pcl_tag VALUES (5, 'anesthesia');
INSERT INTO pcl_tag VALUES (6, 'surgerey');
INSERT INTO pcl_tag VALUES (7, 'pain');
INSERT INTO pcl_tag VALUES (8, 'swelling');
INSERT INTO pcl_tag VALUES (9, 'root');
INSERT INTO pcl_tag VALUES (10, 'canal');
INSERT INTO pcl_tag VALUES (11, 'colon');
INSERT INTO pcl_tag VALUES (12, 'stomach');
INSERT INTO pcl_tag VALUES (13, 'colonoscopy');
INSERT INTO pcl_tag VALUES (14, 'gastroenterologist');
INSERT INTO pcl_tag VALUES (15, 'gastroenterology');
INSERT INTO pcl_tag VALUES (16, 'work');
INSERT INTO pcl_tag VALUES (17, 'endoscopy');
INSERT INTO pcl_tag VALUES (18, 'ulcer');
INSERT INTO pcl_tag VALUES (19, 'cancer');
INSERT INTO pcl_tag VALUES (20, 'biopsy');
INSERT INTO pcl_tag VALUES (21, 'breast');
INSERT INTO pcl_tag VALUES (22, 'screening');
INSERT INTO pcl_tag VALUES (23, 'lasik');
INSERT INTO pcl_tag VALUES (24, 'vision');
INSERT INTO pcl_tag VALUES (25, 'correction');
INSERT INTO pcl_tag VALUES (26, 'laser');
INSERT INTO pcl_tag VALUES (27, 'eye');
INSERT INTO pcl_tag VALUES (28, 'opthamologist');


SELECT pg_catalog.setval('pcl_tag_id_seq', 28, true);






SELECT pg_catalog.setval('pcl_procedure_tags_id_seq', 1, true);





INSERT INTO pcl_question_tags VALUES (1, 2, 1);
INSERT INTO pcl_question_tags VALUES (2, 2, 2);
INSERT INTO pcl_question_tags VALUES (3, 2, 3);
INSERT INTO pcl_question_tags VALUES (4, 2, 4);
INSERT INTO pcl_question_tags VALUES (5, 3, 1);
INSERT INTO pcl_question_tags VALUES (6, 3, 2);
INSERT INTO pcl_question_tags VALUES (7, 3, 3);
INSERT INTO pcl_question_tags VALUES (8, 3, 4);
INSERT INTO pcl_question_tags VALUES (9, 4, 1);
INSERT INTO pcl_question_tags VALUES (10, 4, 2);
INSERT INTO pcl_question_tags VALUES (11, 4, 3);
INSERT INTO pcl_question_tags VALUES (12, 4, 4);
INSERT INTO pcl_question_tags VALUES (13, 5, 1);
INSERT INTO pcl_question_tags VALUES (14, 5, 2);
INSERT INTO pcl_question_tags VALUES (15, 5, 3);
INSERT INTO pcl_question_tags VALUES (16, 5, 4);
INSERT INTO pcl_question_tags VALUES (17, 5, 5);
INSERT INTO pcl_question_tags VALUES (18, 6, 1);
INSERT INTO pcl_question_tags VALUES (19, 6, 2);
INSERT INTO pcl_question_tags VALUES (20, 6, 3);
INSERT INTO pcl_question_tags VALUES (21, 6, 4);
INSERT INTO pcl_question_tags VALUES (22, 6, 5);
INSERT INTO pcl_question_tags VALUES (23, 6, 6);
INSERT INTO pcl_question_tags VALUES (24, 7, 1);
INSERT INTO pcl_question_tags VALUES (25, 7, 2);
INSERT INTO pcl_question_tags VALUES (26, 7, 3);
INSERT INTO pcl_question_tags VALUES (27, 7, 4);
INSERT INTO pcl_question_tags VALUES (28, 7, 5);
INSERT INTO pcl_question_tags VALUES (29, 7, 6);
INSERT INTO pcl_question_tags VALUES (30, 7, 7);
INSERT INTO pcl_question_tags VALUES (31, 7, 8);
INSERT INTO pcl_question_tags VALUES (32, 8, 1);
INSERT INTO pcl_question_tags VALUES (33, 8, 2);
INSERT INTO pcl_question_tags VALUES (34, 8, 3);
INSERT INTO pcl_question_tags VALUES (35, 8, 4);
INSERT INTO pcl_question_tags VALUES (36, 9, 1);
INSERT INTO pcl_question_tags VALUES (37, 9, 2);
INSERT INTO pcl_question_tags VALUES (38, 9, 3);
INSERT INTO pcl_question_tags VALUES (39, 9, 4);
INSERT INTO pcl_question_tags VALUES (40, 10, 1);
INSERT INTO pcl_question_tags VALUES (41, 10, 2);
INSERT INTO pcl_question_tags VALUES (42, 10, 3);
INSERT INTO pcl_question_tags VALUES (43, 10, 4);
INSERT INTO pcl_question_tags VALUES (44, 11, 9);
INSERT INTO pcl_question_tags VALUES (45, 11, 10);
INSERT INTO pcl_question_tags VALUES (46, 12, 9);
INSERT INTO pcl_question_tags VALUES (47, 12, 10);
INSERT INTO pcl_question_tags VALUES (48, 13, 9);
INSERT INTO pcl_question_tags VALUES (49, 13, 10);
INSERT INTO pcl_question_tags VALUES (50, 14, 9);
INSERT INTO pcl_question_tags VALUES (51, 14, 10);
INSERT INTO pcl_question_tags VALUES (52, 33, 11);
INSERT INTO pcl_question_tags VALUES (53, 33, 12);
INSERT INTO pcl_question_tags VALUES (54, 33, 13);
INSERT INTO pcl_question_tags VALUES (55, 33, 14);
INSERT INTO pcl_question_tags VALUES (56, 33, 15);
INSERT INTO pcl_question_tags VALUES (57, 34, 11);
INSERT INTO pcl_question_tags VALUES (58, 34, 12);
INSERT INTO pcl_question_tags VALUES (59, 34, 13);
INSERT INTO pcl_question_tags VALUES (60, 34, 14);
INSERT INTO pcl_question_tags VALUES (61, 34, 15);
INSERT INTO pcl_question_tags VALUES (62, 35, 11);
INSERT INTO pcl_question_tags VALUES (63, 35, 12);
INSERT INTO pcl_question_tags VALUES (64, 35, 13);
INSERT INTO pcl_question_tags VALUES (65, 35, 14);
INSERT INTO pcl_question_tags VALUES (66, 35, 15);
INSERT INTO pcl_question_tags VALUES (67, 36, 11);
INSERT INTO pcl_question_tags VALUES (68, 36, 12);
INSERT INTO pcl_question_tags VALUES (69, 36, 13);
INSERT INTO pcl_question_tags VALUES (70, 36, 14);
INSERT INTO pcl_question_tags VALUES (71, 36, 15);
INSERT INTO pcl_question_tags VALUES (72, 37, 11);
INSERT INTO pcl_question_tags VALUES (73, 37, 12);
INSERT INTO pcl_question_tags VALUES (74, 37, 13);
INSERT INTO pcl_question_tags VALUES (75, 37, 14);
INSERT INTO pcl_question_tags VALUES (76, 37, 15);
INSERT INTO pcl_question_tags VALUES (77, 38, 11);
INSERT INTO pcl_question_tags VALUES (78, 38, 12);
INSERT INTO pcl_question_tags VALUES (79, 38, 13);
INSERT INTO pcl_question_tags VALUES (80, 38, 14);
INSERT INTO pcl_question_tags VALUES (81, 38, 15);
INSERT INTO pcl_question_tags VALUES (82, 39, 11);
INSERT INTO pcl_question_tags VALUES (83, 39, 12);
INSERT INTO pcl_question_tags VALUES (84, 39, 13);
INSERT INTO pcl_question_tags VALUES (85, 39, 14);
INSERT INTO pcl_question_tags VALUES (86, 39, 15);
INSERT INTO pcl_question_tags VALUES (87, 40, 11);
INSERT INTO pcl_question_tags VALUES (88, 40, 12);
INSERT INTO pcl_question_tags VALUES (89, 40, 13);
INSERT INTO pcl_question_tags VALUES (90, 40, 14);
INSERT INTO pcl_question_tags VALUES (91, 40, 15);
INSERT INTO pcl_question_tags VALUES (92, 41, 11);
INSERT INTO pcl_question_tags VALUES (93, 41, 12);
INSERT INTO pcl_question_tags VALUES (94, 41, 13);
INSERT INTO pcl_question_tags VALUES (95, 41, 14);
INSERT INTO pcl_question_tags VALUES (96, 41, 15);
INSERT INTO pcl_question_tags VALUES (97, 42, 11);
INSERT INTO pcl_question_tags VALUES (98, 42, 12);
INSERT INTO pcl_question_tags VALUES (99, 42, 13);
INSERT INTO pcl_question_tags VALUES (100, 42, 14);
INSERT INTO pcl_question_tags VALUES (101, 42, 15);
INSERT INTO pcl_question_tags VALUES (102, 43, 11);
INSERT INTO pcl_question_tags VALUES (103, 43, 12);
INSERT INTO pcl_question_tags VALUES (104, 43, 13);
INSERT INTO pcl_question_tags VALUES (105, 43, 14);
INSERT INTO pcl_question_tags VALUES (106, 43, 15);
INSERT INTO pcl_question_tags VALUES (107, 43, 16);
INSERT INTO pcl_question_tags VALUES (108, 44, 11);
INSERT INTO pcl_question_tags VALUES (109, 44, 12);
INSERT INTO pcl_question_tags VALUES (110, 44, 14);
INSERT INTO pcl_question_tags VALUES (111, 44, 15);
INSERT INTO pcl_question_tags VALUES (112, 44, 17);
INSERT INTO pcl_question_tags VALUES (113, 44, 18);
INSERT INTO pcl_question_tags VALUES (114, 44, 19);
INSERT INTO pcl_question_tags VALUES (115, 51, 20);
INSERT INTO pcl_question_tags VALUES (116, 45, 11);
INSERT INTO pcl_question_tags VALUES (117, 45, 12);
INSERT INTO pcl_question_tags VALUES (118, 45, 14);
INSERT INTO pcl_question_tags VALUES (119, 45, 15);
INSERT INTO pcl_question_tags VALUES (120, 45, 17);
INSERT INTO pcl_question_tags VALUES (121, 45, 18);
INSERT INTO pcl_question_tags VALUES (122, 45, 19);
INSERT INTO pcl_question_tags VALUES (123, 46, 11);
INSERT INTO pcl_question_tags VALUES (124, 46, 12);
INSERT INTO pcl_question_tags VALUES (125, 46, 14);
INSERT INTO pcl_question_tags VALUES (126, 46, 15);
INSERT INTO pcl_question_tags VALUES (127, 46, 17);
INSERT INTO pcl_question_tags VALUES (128, 46, 18);
INSERT INTO pcl_question_tags VALUES (129, 46, 19);
INSERT INTO pcl_question_tags VALUES (130, 47, 11);
INSERT INTO pcl_question_tags VALUES (131, 47, 12);
INSERT INTO pcl_question_tags VALUES (132, 47, 14);
INSERT INTO pcl_question_tags VALUES (133, 47, 15);
INSERT INTO pcl_question_tags VALUES (134, 47, 17);
INSERT INTO pcl_question_tags VALUES (135, 47, 18);
INSERT INTO pcl_question_tags VALUES (136, 47, 19);
INSERT INTO pcl_question_tags VALUES (137, 48, 11);
INSERT INTO pcl_question_tags VALUES (138, 48, 12);
INSERT INTO pcl_question_tags VALUES (139, 48, 14);
INSERT INTO pcl_question_tags VALUES (140, 48, 15);
INSERT INTO pcl_question_tags VALUES (141, 48, 17);
INSERT INTO pcl_question_tags VALUES (142, 48, 18);
INSERT INTO pcl_question_tags VALUES (143, 48, 19);
INSERT INTO pcl_question_tags VALUES (144, 49, 11);
INSERT INTO pcl_question_tags VALUES (145, 49, 12);
INSERT INTO pcl_question_tags VALUES (146, 49, 14);
INSERT INTO pcl_question_tags VALUES (147, 49, 15);
INSERT INTO pcl_question_tags VALUES (148, 49, 17);
INSERT INTO pcl_question_tags VALUES (149, 49, 18);
INSERT INTO pcl_question_tags VALUES (150, 49, 19);
INSERT INTO pcl_question_tags VALUES (151, 50, 11);
INSERT INTO pcl_question_tags VALUES (152, 50, 12);
INSERT INTO pcl_question_tags VALUES (153, 50, 14);
INSERT INTO pcl_question_tags VALUES (154, 50, 15);
INSERT INTO pcl_question_tags VALUES (155, 50, 17);
INSERT INTO pcl_question_tags VALUES (156, 50, 18);
INSERT INTO pcl_question_tags VALUES (157, 50, 19);
INSERT INTO pcl_question_tags VALUES (158, 51, 11);
INSERT INTO pcl_question_tags VALUES (159, 51, 12);
INSERT INTO pcl_question_tags VALUES (160, 51, 14);
INSERT INTO pcl_question_tags VALUES (161, 51, 15);
INSERT INTO pcl_question_tags VALUES (162, 51, 17);
INSERT INTO pcl_question_tags VALUES (163, 51, 18);
INSERT INTO pcl_question_tags VALUES (164, 51, 19);
INSERT INTO pcl_question_tags VALUES (165, 52, 11);
INSERT INTO pcl_question_tags VALUES (166, 52, 12);
INSERT INTO pcl_question_tags VALUES (167, 52, 14);
INSERT INTO pcl_question_tags VALUES (168, 52, 15);
INSERT INTO pcl_question_tags VALUES (169, 52, 17);
INSERT INTO pcl_question_tags VALUES (170, 52, 18);
INSERT INTO pcl_question_tags VALUES (171, 52, 19);
INSERT INTO pcl_question_tags VALUES (179, 53, 11);
INSERT INTO pcl_question_tags VALUES (180, 53, 12);
INSERT INTO pcl_question_tags VALUES (181, 53, 14);
INSERT INTO pcl_question_tags VALUES (182, 53, 15);
INSERT INTO pcl_question_tags VALUES (183, 53, 17);
INSERT INTO pcl_question_tags VALUES (184, 53, 18);
INSERT INTO pcl_question_tags VALUES (185, 53, 19);
INSERT INTO pcl_question_tags VALUES (186, 54, 1);
INSERT INTO pcl_question_tags VALUES (187, 54, 2);
INSERT INTO pcl_question_tags VALUES (188, 54, 3);
INSERT INTO pcl_question_tags VALUES (189, 54, 4);
INSERT INTO pcl_question_tags VALUES (194, 55, 1);
INSERT INTO pcl_question_tags VALUES (195, 55, 2);
INSERT INTO pcl_question_tags VALUES (196, 55, 3);
INSERT INTO pcl_question_tags VALUES (197, 55, 4);
INSERT INTO pcl_question_tags VALUES (198, 56, 1);
INSERT INTO pcl_question_tags VALUES (199, 56, 2);
INSERT INTO pcl_question_tags VALUES (200, 56, 3);
INSERT INTO pcl_question_tags VALUES (201, 56, 4);
INSERT INTO pcl_question_tags VALUES (202, 57, 19);
INSERT INTO pcl_question_tags VALUES (203, 57, 20);
INSERT INTO pcl_question_tags VALUES (204, 57, 21);
INSERT INTO pcl_question_tags VALUES (205, 57, 22);
INSERT INTO pcl_question_tags VALUES (206, 58, 19);
INSERT INTO pcl_question_tags VALUES (207, 58, 20);
INSERT INTO pcl_question_tags VALUES (208, 58, 21);
INSERT INTO pcl_question_tags VALUES (209, 58, 22);
INSERT INTO pcl_question_tags VALUES (210, 59, 19);
INSERT INTO pcl_question_tags VALUES (211, 59, 20);
INSERT INTO pcl_question_tags VALUES (212, 59, 21);
INSERT INTO pcl_question_tags VALUES (213, 59, 22);
INSERT INTO pcl_question_tags VALUES (214, 60, 19);
INSERT INTO pcl_question_tags VALUES (215, 60, 20);
INSERT INTO pcl_question_tags VALUES (216, 60, 21);
INSERT INTO pcl_question_tags VALUES (217, 60, 22);
INSERT INTO pcl_question_tags VALUES (218, 61, 19);
INSERT INTO pcl_question_tags VALUES (219, 61, 20);
INSERT INTO pcl_question_tags VALUES (220, 61, 21);
INSERT INTO pcl_question_tags VALUES (221, 61, 22);
INSERT INTO pcl_question_tags VALUES (222, 62, 19);
INSERT INTO pcl_question_tags VALUES (223, 62, 20);
INSERT INTO pcl_question_tags VALUES (224, 62, 21);
INSERT INTO pcl_question_tags VALUES (225, 62, 22);
INSERT INTO pcl_question_tags VALUES (226, 62, 7);
INSERT INTO pcl_question_tags VALUES (227, 63, 19);
INSERT INTO pcl_question_tags VALUES (228, 63, 20);
INSERT INTO pcl_question_tags VALUES (229, 63, 21);
INSERT INTO pcl_question_tags VALUES (230, 63, 22);
INSERT INTO pcl_question_tags VALUES (231, 64, 19);
INSERT INTO pcl_question_tags VALUES (232, 64, 20);
INSERT INTO pcl_question_tags VALUES (233, 64, 21);
INSERT INTO pcl_question_tags VALUES (234, 64, 22);
INSERT INTO pcl_question_tags VALUES (235, 65, 19);
INSERT INTO pcl_question_tags VALUES (236, 65, 20);
INSERT INTO pcl_question_tags VALUES (237, 65, 21);
INSERT INTO pcl_question_tags VALUES (238, 65, 22);
INSERT INTO pcl_question_tags VALUES (239, 66, 19);
INSERT INTO pcl_question_tags VALUES (240, 66, 20);
INSERT INTO pcl_question_tags VALUES (241, 66, 21);
INSERT INTO pcl_question_tags VALUES (242, 66, 22);
INSERT INTO pcl_question_tags VALUES (243, 67, 19);
INSERT INTO pcl_question_tags VALUES (244, 67, 20);
INSERT INTO pcl_question_tags VALUES (245, 67, 21);
INSERT INTO pcl_question_tags VALUES (246, 67, 22);
INSERT INTO pcl_question_tags VALUES (247, 68, 23);
INSERT INTO pcl_question_tags VALUES (248, 68, 24);
INSERT INTO pcl_question_tags VALUES (249, 68, 25);
INSERT INTO pcl_question_tags VALUES (250, 68, 26);
INSERT INTO pcl_question_tags VALUES (251, 68, 27);
INSERT INTO pcl_question_tags VALUES (252, 68, 28);
INSERT INTO pcl_question_tags VALUES (253, 69, 23);
INSERT INTO pcl_question_tags VALUES (254, 69, 24);
INSERT INTO pcl_question_tags VALUES (255, 69, 25);
INSERT INTO pcl_question_tags VALUES (256, 69, 26);
INSERT INTO pcl_question_tags VALUES (257, 69, 27);
INSERT INTO pcl_question_tags VALUES (258, 69, 28);
INSERT INTO pcl_question_tags VALUES (259, 70, 23);
INSERT INTO pcl_question_tags VALUES (260, 70, 24);
INSERT INTO pcl_question_tags VALUES (261, 70, 25);
INSERT INTO pcl_question_tags VALUES (262, 70, 26);
INSERT INTO pcl_question_tags VALUES (263, 70, 27);
INSERT INTO pcl_question_tags VALUES (264, 70, 28);
INSERT INTO pcl_question_tags VALUES (265, 71, 23);
INSERT INTO pcl_question_tags VALUES (266, 71, 24);
INSERT INTO pcl_question_tags VALUES (267, 71, 25);
INSERT INTO pcl_question_tags VALUES (268, 71, 26);
INSERT INTO pcl_question_tags VALUES (269, 71, 27);
INSERT INTO pcl_question_tags VALUES (270, 71, 28);
INSERT INTO pcl_question_tags VALUES (271, 72, 23);
INSERT INTO pcl_question_tags VALUES (272, 72, 24);
INSERT INTO pcl_question_tags VALUES (273, 72, 25);
INSERT INTO pcl_question_tags VALUES (274, 72, 26);
INSERT INTO pcl_question_tags VALUES (275, 72, 27);
INSERT INTO pcl_question_tags VALUES (276, 72, 28);
INSERT INTO pcl_question_tags VALUES (277, 73, 23);
INSERT INTO pcl_question_tags VALUES (278, 73, 24);
INSERT INTO pcl_question_tags VALUES (279, 73, 25);
INSERT INTO pcl_question_tags VALUES (280, 73, 26);
INSERT INTO pcl_question_tags VALUES (281, 73, 27);
INSERT INTO pcl_question_tags VALUES (282, 73, 28);
INSERT INTO pcl_question_tags VALUES (283, 74, 23);
INSERT INTO pcl_question_tags VALUES (284, 74, 24);
INSERT INTO pcl_question_tags VALUES (285, 74, 25);
INSERT INTO pcl_question_tags VALUES (286, 74, 26);
INSERT INTO pcl_question_tags VALUES (287, 74, 27);
INSERT INTO pcl_question_tags VALUES (288, 74, 28);
INSERT INTO pcl_question_tags VALUES (289, 75, 23);
INSERT INTO pcl_question_tags VALUES (290, 75, 24);
INSERT INTO pcl_question_tags VALUES (291, 75, 25);
INSERT INTO pcl_question_tags VALUES (292, 75, 26);
INSERT INTO pcl_question_tags VALUES (293, 75, 27);
INSERT INTO pcl_question_tags VALUES (294, 75, 28);
INSERT INTO pcl_question_tags VALUES (295, 76, 23);
INSERT INTO pcl_question_tags VALUES (296, 76, 24);
INSERT INTO pcl_question_tags VALUES (297, 76, 25);
INSERT INTO pcl_question_tags VALUES (298, 76, 26);
INSERT INTO pcl_question_tags VALUES (299, 76, 27);
INSERT INTO pcl_question_tags VALUES (300, 76, 28);
INSERT INTO pcl_question_tags VALUES (301, 77, 23);
INSERT INTO pcl_question_tags VALUES (302, 77, 24);
INSERT INTO pcl_question_tags VALUES (303, 77, 25);
INSERT INTO pcl_question_tags VALUES (304, 77, 26);
INSERT INTO pcl_question_tags VALUES (305, 77, 27);
INSERT INTO pcl_question_tags VALUES (306, 77, 28);
INSERT INTO pcl_question_tags VALUES (307, 78, 23);
INSERT INTO pcl_question_tags VALUES (308, 78, 24);
INSERT INTO pcl_question_tags VALUES (309, 78, 25);
INSERT INTO pcl_question_tags VALUES (310, 78, 26);
INSERT INTO pcl_question_tags VALUES (311, 78, 27);
INSERT INTO pcl_question_tags VALUES (312, 78, 28);
INSERT INTO pcl_question_tags VALUES (313, 79, 23);
INSERT INTO pcl_question_tags VALUES (314, 79, 24);
INSERT INTO pcl_question_tags VALUES (315, 79, 25);
INSERT INTO pcl_question_tags VALUES (316, 79, 26);
INSERT INTO pcl_question_tags VALUES (317, 79, 27);
INSERT INTO pcl_question_tags VALUES (318, 79, 28);
INSERT INTO pcl_question_tags VALUES (319, 80, 23);
INSERT INTO pcl_question_tags VALUES (320, 80, 24);
INSERT INTO pcl_question_tags VALUES (321, 80, 25);
INSERT INTO pcl_question_tags VALUES (322, 80, 26);
INSERT INTO pcl_question_tags VALUES (323, 80, 27);
INSERT INTO pcl_question_tags VALUES (324, 80, 28);
INSERT INTO pcl_question_tags VALUES (325, 81, 23);
INSERT INTO pcl_question_tags VALUES (326, 81, 24);
INSERT INTO pcl_question_tags VALUES (327, 81, 25);
INSERT INTO pcl_question_tags VALUES (328, 81, 26);
INSERT INTO pcl_question_tags VALUES (329, 81, 27);
INSERT INTO pcl_question_tags VALUES (330, 81, 28);
INSERT INTO pcl_question_tags VALUES (331, 82, 23);
INSERT INTO pcl_question_tags VALUES (332, 82, 24);
INSERT INTO pcl_question_tags VALUES (333, 82, 25);
INSERT INTO pcl_question_tags VALUES (334, 82, 26);
INSERT INTO pcl_question_tags VALUES (335, 82, 27);
INSERT INTO pcl_question_tags VALUES (336, 82, 28);


--
-- Name: pcl_question_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('pcl_question_tags_id_seq', 336, true);






INSERT INTO pcl_vote VALUES (9, 74, 1, 2, 10, 1371668468);
INSERT INTO pcl_vote VALUES (21, 73, 1, 8, 10, 1371675794);
INSERT INTO pcl_vote VALUES (22, 77, 1, 8, 10, 1371675797);
INSERT INTO pcl_vote VALUES (23, 70, 1, 8, 10, 1371675799);
INSERT INTO pcl_vote VALUES (24, 68, 1, 8, 10, 1371675819);


--
-- Name: pcl_vote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('pcl_vote_id_seq', 26, true);












CREATE OR REPLACE FUNCTION procedure_forum_search(_query text) RETURNS TABLE(tid integer, rank real)
    LANGUAGE sql
    AS $_$

select tid, sum(myRank) as rank from (
SELECT p.topic_id as tid, ts_rank_cd(to_tsvector( p.body ), query) AS myRank
FROM pcl_forumpost as p, to_tsquery( $1 ) query
WHERE query @@ to_tsvector( p.body )
union
SELECT t.id as tid, ts_rank_cd(to_tsvector( t.title ), query) AS myRank
FROM pcl_forumtopic as t, to_tsquery( $1 ) query
WHERE query @@ to_tsvector( t.title )
) as temp
group by tid
order by rank desc
$_$;






CREATE FUNCTION procedure_query_and_rank(_query text) RETURNS TABLE(pid integer, rank real)
    LANGUAGE sql
    AS $_$
select pid, sum(myRank) as rank from (
SELECT qp.procedure_id as pid, ts_rank_cd(q.tsvec, query) AS myRank
FROM pcl_question as q, to_tsquery( $1 ) query, pcl_procedurequestionscore as qp
WHERE query @@ q.tsvec
and qp.question_id = q.id
) as temp
group by pid
order by rank desc
$_$;

















