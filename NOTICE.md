# Data notice

This project uses the [Mammographic Image Analysis Society (MIAS)
database v1.21](https://doi.org/10.17863/CAM.105113). The data itself
is not included in this repository — see `scripts/download_mini_mias.py`
to fetch it from the official source.

## Citation

For the paper:
J Suckling et al (1994) "The Mammographic Image Analysis Society
Digital Mammogram Database" Excerpta Medica. International Congress
Series 1069 pp375-378.

For the database:
Suckling, J. et al. (2015) 'Mammographic Image Analysis Society (MIAS)
database v1.21'. Apollo - University of Cambridge Repository.
doi:10.17863/CAM.105113.

## Licensing note

There is a discrepancy between two sources worth stating plainly
rather than glossing over:

- The Cambridge Apollo repository record lists this dataset as
  licensed under **CC BY (Attribution 2.0 UK: England & Wales)**.
- The original MIAS Licence Agreement, bundled inside the downloaded
  archive itself, restricts use to **"research purposes ONLY"** and
  does not explicitly grant redistribution rights (see full text
  below).

Because these two statements don't obviously reconcile, this project
does not rehost or redistribute the dataset. The download script
fetches directly from the official Cambridge Apollo record rather than
bundling a copy here, and this project's own use of the data is for
research/educational purposes — consistent with the original
agreement regardless of which licensing statement is ultimately
controlling. If you need certainty on redistribution rights beyond
that, contact the depositors or Cambridge's repository team directly.

## Original MIAS Licence Agreement

*(as bundled in the downloaded archive, reproduced here in full per
its own citation requirement)*

```
              MAMMOGRAPHIC IMAGE ANALYSIS SOCIETY
                     MiniMammographic Database

                       LICENCE AGREEMENT


This is a legal agreement between you, the end user and the
Mammographic Image Analysis Society ("MIAS"). Upon installing the
MiniMammographic database (the "DATABASE") on your system you are
agreeing to be bound by the terms of this Agreement.

1. GRANT OF LICENCE
MIAS grants you the right to use the DATABASE, for research purposes
ONLY. For this purpose, you may edit, format, or otherwise modify the
DATABASE provided that the unmodified portions of the DATABASE included
in a modified work shall remain subject to the terms of this Agreement.

1. COPYRIGHT
The DATABASE is owned by MIAS and is protected by United Kingdom
copyright laws, international treaty provisions and all other
applicable national laws. Therefore you must treat the DATABASE
like any other copyrighted material. If the DATABASE is used in any
publications then reference must be made to the DATABASE within that
publication.

1. OTHER RESTRICTIONS
You may not rent, lease or sell the DATABASE.

1. LIABILITY
To the maximum extent permitted by applicable law, MIAS shall not
be liable for damages, other than death or personal injury,
whatsoever (including without limitation, damages for negligence,
loss of business, profits, business interruption, loss of
business information, or other pecuniary loss) arising out of the
use of or inability to use this DATABASE, even if MIAS has been
advised of the possibility of such damages. In any case, MIAS's
entire liability under this Agreement shall be limited to the
amount actually paid by you or your assignor, as the case may be,
for the DATABASE.
```