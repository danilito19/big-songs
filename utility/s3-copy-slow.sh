
# terminal command to copy data to S3 for a range of folders
# very slow command!
ls -R . | awk '
/:$/&&f{s=$0;f=0}
/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}
NF&&f{ print s"/"$0 }' | grep -i "\/[M-Z]\/.\/.\/\w*\.h5" | xargs -I {} aws s3 cp {} s3://songs-data-all

#sync command example
aws s3 sync s3://songs-data/data/Z/Z/Z s3://songs-test

## terminal command for counting objects in bucket
aws s3 ls s3://songs-data-all/ --recursive | wc -l 