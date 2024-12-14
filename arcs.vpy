pagesize --landscape letter
eval "w,h=prop.vp_page_size; cw=w/2; ch=h/2"
eval "r=24"

begin
repeat 96
    eval "start=1/6*pi; end=2/6*pi"
    eval "offset=_i*2/6*pi"
    eval "ri=_i//6*8"
    arc %cw% %ch% %r+ri% %r+ri% %start+offset%rad %end+offset%rad
end

stat
show
