pagesize --landscape letter
eval "w,h=prop.vp_page_size; cw=w/2; ch=h/2"
eval "r=192"

begin
    # 360/angle
    repeat 30
    eval "angle=radians(12*_i); offset=6*_i; x=cw+r*sin(angle)+offset; y=ch+r*cos(angle)+offset"
    eval "d=radians(15); l=18; xv=l*sin(d); yv=l*cos(d); p1=(x-xv, y-yv); p2=(x+xv, y+yv)"
    line %p1[0]% %p1[1]% %p2[0]% %p2[1]%
end

squiggles
lcopy 1 new
lcopy 1 new
translate -- -48 -48
translate --layer 2 -- -24 -24
translate --layer 3 -- -60 -48
stat
show
