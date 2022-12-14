"""empty message

Revision ID: 2b5137c067f6
Revises: ba168df44dec
Create Date: 2022-12-04 14:28:26.736625

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "2b5137c067f6"
down_revision = "ba168df44dec"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
