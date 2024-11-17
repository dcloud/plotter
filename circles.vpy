pagesize --landscape letter
eval "w,h=prop.vp_page_size; cw=w/2; ch=h/2"
eval "r=96"
# circle %cw% %ch% %r%
translate --layer 2 2in 3in
begin
    # 360/angle
    repeat 12
    eval "angle=radians(30*_i); x=cw+r*sin(angle); y=ch+r*cos(angle)"
    circle %x% %y% %r%
    # text --position %w/4% %24+24*_i% "x: %x%, y: %y%"
end
show
