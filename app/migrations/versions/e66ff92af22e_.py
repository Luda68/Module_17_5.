"""empty message

Revision ID: e66ff92af22e
Revises: 603fa73d3eea
Create Date: 2024-12-11 15:16:26.634273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e66ff92af22e'
down_revision: Union[str, None] = '603fa73d3eea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
