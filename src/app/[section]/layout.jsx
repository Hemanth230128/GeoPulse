import { notFound } from 'next/navigation';
import { navConfig } from '@/config/nav';
import { Sidebar } from '@/components/layout/sidebar';

export default function SectionLayout({ children, params }) {
  const { section } = params;
  const sidebarNav = navConfig.sidebarNav[section];

  if (!sidebarNav) {
    notFound();
  }

  return (
    <div className="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col md:flex-row gap-8 py-8 md:py-12">
        <Sidebar items={sidebarNav} sectionTitle={section} />
        <div className="flex-1 min-w-0">
          {children}
        </div>
      </div>
    </div>
  );
}
