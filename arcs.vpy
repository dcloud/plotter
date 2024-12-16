pagesize --landscape letter

eval "w,h=prop.vp_page_size; cw=w/2; ch=h/2"
eval "r=24; rpt=96; pos=r+rpt//6*8;"

begin
repeat %rpt%
    eval "itg=_i//6; m=pi*1/(itg+4); start=1/8*pi-m; end=2/6*pi-m; offset=_i*2/6*pi; ri=itg*8"
    arc %pos% %pos% %r+ri% %r+ri% %start+offset%rad %end+offset%rad
end

lcopy -m 1 new
lcopy -m 1 new
lcopy -m 1 new
translate -l 2 %pos*2% 0
translate -l 3 %2*pos*2% 0
translate -l 4 0 %pos*2%

color black

stat
show
