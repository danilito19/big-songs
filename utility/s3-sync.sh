# bash commands to split data copying from EC2 to S3 for three nodes


# for folders A-I
for i in {A..I}; do
    for j in {A..Z}; do
        for k in {A..Z}; do
            aws s3 sync s3://songs-data/data/$i/$j/$k s3://songs-data-all
        done
    done
done

# for folders J - Q
for i in {J..Q}; do
    for j in {A..Z}; do
        for k in {A..Z}; do
            aws s3 sync s3://songs-data/data/$i/$j/$k s3://songs-data-all
        done
    done
done

#for folders R-Z
for i in {R..Z}; do
    for j in {A..Z}; do
        for k in {A..Z}; do
            aws s3 sync s3://songs-data/data/$i/$j/$k s3://songs-data-all
        done
    done
done
