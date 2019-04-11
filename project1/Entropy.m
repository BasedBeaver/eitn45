function H=Entropy(P)
% The Entropy function H(X)
%
% P column vector: the vector is the probability distribution.
% P matrix: Each column vector is a probability distribution
%P scalar: The binary entropy function of [P; 1-P]
%P row vector: Each position gives binary entropy function

[rownum, colnum] = size(P);

%-------%
H = [];
if (rownum > 1) && (colnum > 1);
    for i = 1:colnum
        v = P(:, i);
        H = [H col_entropy(v)];
    end
elseif colnum == 1 && rownum > 1;
    H = col_entropy(P);
elseif rownum == 1 && colnum > 1;
    for i = 1:colnum
        H = [H bin_entropy(P(i))];
    end
else 
    H = bin_entropy(P);
end
end

%-------%
function H = col_entropy(col_v)
row_v = col_v.';
colnum = size(row_v);
H = 0;
for i = 1:colnum(2);
    H = H + (-row_v(i) * logg2(row_v(i)));
end
end

%-------%
function h = bin_entropy(S)
h = -S*logg2(S) - (1-S)*logg2((1-S));
end

%-------%
function x = logg2(nbr)
if nbr == 0;
    x = 0;
else
    x = log2(nbr);
end
end

