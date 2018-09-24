from django.conf.urls import patterns, url, include

from pcl import views, views_user, views_common, views_forum




urlpatterns = patterns('',

    url(r'^$',                                  views.index,                name='idx'),
    
    
    url(r'^search/$',                           views.search,               name='search'),
    url(r'^search/(?P<query>.+)',               views.searchQuery,          name='search'),
    
    # url(r'^procedure/(?P<pid>\d+)$',            views.procedure,            name='procedure'),

    url(r'^question/star/$',                    views.questionStar,         name='qStar'),

    url(r'^procedures/$',                       views.procedures,           name='procs'),
    

    url(r'^user/signup/$',                      views_user.userSignup,        name='uSignup'   ),
    url(r'^user/login/$',                       views_user.userLogin,         name='uLogin'    ),
    url(r'^user/loggedin/$',                    views_user.userLoggedIn,      name='uLoggedIn' ),
    url(r'^user/logout/$',                      views_user.userLogout,        name='uLogout'   ),
    url(r'^user/verify/(?P<token>\w+)',         views_user.userVerify,        name='uVerify'   ),
    
    
    url(r'^user/forgot/$',                      views_user.userForgotPwd,       name='uForgot'),
    url(r'^user/reset/set/$',                   views_user.userResetSet,        name='uResetSet'),
    url(r'^user/reset/(?P<token>\w+)',          views_user.userResetPwd,        name='uReset'),
    
    
    url(r'^user/lists/$',                       views_user.userLists,         name='MyChecklists'),
    url(r'^user/list/add/$',                    views_user.userListAdd,       name='uListAdd'),
    url(r'^user/list/del/$',                    views_user.userListDel,       name='uListDel'),
    url(r'^user/list/send/$',                   views_user.userListSend,      name='uListSend'),

    

    url(r'^user/list/question/add/$',           views_user.userQuestionAdd,       name='uListQAdd'),
    url(r'^user/list/question/del/$',           views_user.userQuestionDel,       name='uListQDel'),
    url(r'^user/list/question/reorder/$',       views_user.userQuestionReorder,   name='uListQDel'),
    
    url(r'^user/list/(?P<token>\w+)/',          views_user.userListShow,      name='uList'),
    
    url(r'^user/profile/$',                     views_user.userProfile, name='Profile'),



    url(r'^list/print/$',                       views.listPrint,       name='listPrint'),


    url(r'^quick-list/$',                       views.quickList,       name='quickList'),



    url(r'^share/(?P<token>\w+)/',          views_user.userListShow,      name='uList'),











    url(r'^forum/$',                              views_forum.forumAreas,       name='forum'       ),
    url(r'^forum/search/(?P<query>.*)$',          views_forum.forumTopicsSearch,    name='forumTopicsSearch'  ),

    url(r'^forum/area-(?P<area>.+?)/$',                        views_forum.forumProcedures,  name='forumProcs'  ),    
    url(r'^forum/area-(?P<area>.+?)/search/(?P<query>.*)$',    views_forum.forumTopicsSearch,    {'pid': -1 }   ),



    url(r'^forum/(?P<pid>\d+)-([\w\-]+)/add/$',                  views_forum.forumTopicAdd,      name='forumTopicAdd'  ),
    url(r'^forum/(?P<pid>\d+)-([\w\-]+)/search/(?P<query>.*)$',  views_forum.forumTopicsSearch,  name='forumTopicsSearch'  ),
    
    
    
    url(r'^forum/(\d+)-([\w\-]+)/(?P<tid>\d+)/add/$',     views_forum.forumPostAdd,    name='forumPostAdd'   ),
    url(r'^forum/(\d+)-([\w\-]+)/(?P<tid>\d+)/del/$',     views_forum.forumTopicDel,   name='forumTopicDel'  ),
    url(r'^forum/(\d+)-([\w\-]+)/(?P<tid>\d+)/flag/$',    views_forum.forumTopicFlag,  name='forumTopicFlag' ),
    url(r'^forum/(\d+)-([\w\-]+)/(?P<tid>\d+)/edit/$',    views_forum.forumTopicEdit,    name='forumTopicEdit'   ),

    url(r'^forum/(\d+)-([\w\-]+)/(?P<tid>\d+)/$',         views_forum.forumTopic,     name='forumTopic'    ),
    
    
    
    url(r'^forum/(?P<pid>\d+)-([\w\-]+)/$',      views_forum.forumTopics,      name='forumTopics' ),
    
    
    


    url(r'^data/procedures/',                   views.dataProcedures,      name='dProc'),


    
    url(r'^contact/send/',              views.sendContact,       name='SendContact'),
    

    url(r'^blog/',                      views.blog,  name='blog' ),
    
    url(r'^about/',                     views_common.about,             name='about' ),
    url(r'^tos/',                       views_common.tos,               name='tos' ),
    url(r'^general/(?P<what>\w*)/$',    views_common.general,           name='general' ),


    url(r'^404/',                       views.custom_404,               name='404' ),

)
