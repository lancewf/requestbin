pkg_name=requestbin
pkg_origin=lancewf
pkg_version="0.1.0"
pkg_maintainer="Lance Finfrock <lfinfrock@chef.io>"
pkg_license=('Apache-2.0')
pkg_source=""
pkg_deps=(core/coreutils core/python2)
pkg_build_deps=(core/virtualenv core/gcc)

pkg_svc_user=root
pkg_svc_group=$pkg_svc_user

pkg_exports=(
   [port]=http.listen.port
   [local_only]=http.listen.local_only
)

pkg_binds=(

)

do_unpack() {
    mkdir -p $pkg_prefix/app
    build_line "Copying project data to $pkg_prefix/app"
    cp -r ${PLAN_CONTEXT}/../requestbin $pkg_prefix/app/
    cp ${PLAN_CONTEXT}/../*.py $pkg_prefix/app/
    cp ${PLAN_CONTEXT}/../requirements.txt $pkg_prefix/app/
}

do_build(){
  return 0
}

do_install() {
    cd $pkg_prefix/app/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
}
