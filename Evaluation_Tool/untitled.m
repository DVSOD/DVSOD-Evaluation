saving = zeros(1,216);
saving(1) = 2000;
for a = 2:216
    saving(a) = saving(a-1)+(saving(a-1)*0.0625/12)+200;
end
saving(end)

art = zeros(1,22);
scince = zeros(1,22);
engineering = zeros(1,22);
art(1) = 5550;
scince(1) = 6150;
engineerng(1) = 6550;
for b = 2:22
    art(b) = art(b-1)+(art(b-1)*0.07);
    scince(b) = scince(b-1)+(scince(b-1)*0.07);
    engineering(b) = engineering(b-1)+(engineering(b-1)*0.07);
    engineering(b)
end
Tart = sum(art(end));
Tscince = sum(scince(end));
Tengineering = sum(engineering(end));